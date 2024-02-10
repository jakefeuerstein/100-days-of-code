from flask import Flask, render_template, request
import requests
import smtplib

g_email = ""
y_email = ""
password =""

app = Flask(__name__)

blog_url = "https://api.npoint.io/"
all_posts = requests.get(blog_url).json()

@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        submitted = True
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=g_email, password=password)
            connection.sendmail(
                from_addr=g_email,
                to_addrs=g_email,
                msg=f"Subject:message from {request.form['name']}!"
                    f"\n\n{request.form['message']}"
                    f"contact at {request.form['email']}, {request.form['phone']}"
            )
        return render_template('contact.html', submission=submitted)
    else:
        submitted = False
        return render_template('contact.html', submission=submitted)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = all_posts[post_id-1]
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=False)




