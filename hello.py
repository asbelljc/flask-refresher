from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "The value of __name__ is {}".format(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
