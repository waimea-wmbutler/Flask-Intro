from flask import Flask
from flask import render_template
from flask import redirect
from random import randint

# Create the app
app = Flask(__name__)


@app.get("/")
def home():
    return render_template('pages/home.jinja')

@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

@app.get("/random/")
def random():
    randNum = randint(1, 1000000000000000)
    return render_template('pages/random.jinja', number=randNum)

@app.get("/number/<int:num>")
def analyseNumber(num):
    print(f"You Entered: {num} ")
    return render_template ('pages/number.jinja', number=num)

@app.get("/form/")
@app.get("/form")
def form():
    return render_template ('pages/form.jinja')

@app.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja")
