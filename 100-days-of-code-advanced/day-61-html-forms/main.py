from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def receive_data():
    user = request.form["username"]
    pw = request.form["password"]
    return f'<h1>username: {user}, password: {pw}</h1>'

if __name__ == "__main__":
    app.run(debug=False)
