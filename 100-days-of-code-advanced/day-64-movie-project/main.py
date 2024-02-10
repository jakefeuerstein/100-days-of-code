from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title

class AddMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField("Add Movie")

class RateMovieForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField("Done")


with app.app_context():
    db.create_all()

    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's "
    #                 "sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to "
    #                 "a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )

    # db.session.add(new_movie)
    # db.session.commit()


    #
    # movie = Movie.query.filter_by(id=1).first()
    #
    # print(movie)

@app.route("/")
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", all_movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_to_edit = request.args.get("movie_to_edit")
    movie = Movie.query.filter_by(title=movie_to_edit).first()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie_to_edit=movie, form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    Movie.query.filter_by(id=movie_id).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)

