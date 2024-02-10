from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def display_guess_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

rand_num = random.randint(0, 10)
print(rand_num)

@app.route("/<int:guess>")
def check_guess_number(guess):
    if guess < rand_num:
        return '<h1 style="color:blue">Too low!</h1>' \
               '<img src="https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif">'
    if guess > rand_num:
        return '<h1 style="color:red">Too high!</h1>' \
               '<img src="https://media.giphy.com/media/P1PemPnyp4g1i/giphy.gif">'
    else:
        return '<h1>Correct!</h1>' \
               '<img src="https://media.giphy.com/media/PS7d4tm1Hq6Sk/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)