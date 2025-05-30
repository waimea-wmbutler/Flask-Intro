from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from random import randint


# Create the app
app = Flask(__name__)


# ----------------------------------
# Home Page - Static
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# About Page - Static
@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

# Random Day Page - Passing Value Through Template
@app.get("/day/")
def random():
    randMon = randMon(1,12)
    randDay = randint(1,31)
    randYear = randint(1944, 1950)
    return render_template(
        'pages/random.jinja',
        year = request.day["year"],
        age = request.day["month"],
        day = request.day["year"]
        )

# Number Page - Gets Value From Root - `Pass Into Template
@app.get("/number/<int:num>")
def analyseNumber(num):
    print(f"You Entered: {num} ")
    return render_template ('pages/number.jinja', number=num)

# Form Page - Static With Form
@app.get("/form/")
@app.get("/form")
def form():
    return render_template ('pages/form.jinja')


# ----------------------------------
# Handle Data From Form
@app.post('/processForm')
def processForm():
    print(f"Form Data: ${request.form}")
    return render_template(
        "pages/formData.jinja",
        name = request.form["name"],
        age = request.form["age"]
    )



# Error Page - Static
@app.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja")
