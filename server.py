import random
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", number=random.randint(0, 1000))


@app.route("/guess/<name>")
def guess(name):
    res_age = requests.get(f"http://api.agify.io?name={name}").json()
    res_gender = requests.get(f"https://api.genderize.io?name={name}").json()
    gender = "dude" if res_gender["gender"] == "male" else "lady"
    name = name.capitalize()

    return render_template("guess.html", name=name, age=res_age["age"], gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
