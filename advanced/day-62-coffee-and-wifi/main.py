from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, ValidationError, URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap(app)


def contains_int(form, field):
    if not any(char.isdigit() for char in field.data):
        raise ValidationError("Input must contain a number")

def contains_ampm(form, field):
    if not "am" in field.data.lower() and not "pm" in field.data.lower():
        raise ValidationError('Input must contain "am" or "pm"')

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_URL = URLField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField('Open time', validators=[DataRequired(), contains_int, contains_ampm])
    closing_time = StringField('Open time', validators=[DataRequired(), contains_int, contains_ampm])
    coffee_rating = SelectField('Coffee rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[DataRequired()])
    power_outlet_rating = SelectField('Power outlet availability', choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', encoding="utf-8") as csv_file:
            new_row = str(
                "\n" +
                form.cafe._value() + "," +
                form.location_URL._value() + "," +
                form.open_time._value() + "," +
                form.closing_time._value() + "," +
                form.coffee_rating.data + "," +
                form.wifi_rating.data + "," +
                form.power_outlet_rating.data
            )
            csv_file.write(new_row)
        return redirect('cafes')
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
