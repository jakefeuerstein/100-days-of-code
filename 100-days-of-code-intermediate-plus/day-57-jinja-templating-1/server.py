from flask import Flask, render_template
import datetime as dt
import requests

GENDER_EP = "https://api.genderize.io?name="
AGE_EP = "https://api.agify.io?name="

app = Flask(__name__)

@app.route('/')
def home():
    current_year = dt.datetime.now().year
    creator = ""
    return render_template("index.html", current_year=current_year, creator=creator)

@app.route('/guess/')
def guess():
    return "Enter a name to predict gender and age"

@app.route('/guess/<name>')
def check_name(name):
    name = "jake"
    gender = requests.get(f"{GENDER_EP}{name}").json()['gender']
    age = requests.get(f"{AGE_EP}{name}").json()['age']
    name = name.capitalize()
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route('/blog/')
def blog():
    blog_url = "https://api.npoint.io/"
    all_posts = requests.get(blog_url).json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)