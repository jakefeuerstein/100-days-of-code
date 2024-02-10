from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Home"

@app.route('/blog/')
def get_blog():
    blog_url = "https://api.npoint.io/"
    global all_posts
    all_posts = requests.get(blog_url).json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:id>')
def get_post(id):
    this_post = all_posts[id - 1]
    return render_template("index.html", this_post=this_post)

if __name__ == "__main__":
    app.run(debug=True)
