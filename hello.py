from flask import Flask
import random

app = Flask(__name__)


answer = random.randint(0, 9)


@app.route("/")
def home():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"
    )


@app.route("/<int:number>")
def guess(number):
    if number == answer:
        return "<h1>You got it!</h1>"
    elif number > answer:
        return "<h1>Too high! You suck!</h1>"
    else:
        return "<h1>Too low! What a moron!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
