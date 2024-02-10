from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email

class LogInForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(), validators.Length(min=6, max=40)])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
Bootstrap(app)
app.secret_key = ""

golden_email = ""
golden_password = ""

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LogInForm()
    if login_form.validate_on_submit():
        if login_form.email.data == golden_email and login_form.password.data == golden_password:
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)