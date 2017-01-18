from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

MADLIB_TEMPLATES = ['madlib.html', 'madlib2.html']


@app.route("/game")
def show_madlib_form():
    """Show the madlib form"""

    response = request.args.get("game")

    if response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/')
def start_here():
    """Homepage."""

    return render_template("home.html")


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/madlib', methods=["GET", "POST"])
def show_madlib():
    """Make the madlib"""
    if request.method == "POST":
        person = request.form.get("person")
        color = request.form.get("color")
        noun = request.form.get("noun")
        adjective = request.form.getlist("adjective")

    else:
        person = request.args.get("person")
        color = request.args.get("color")
        noun = request.args.get("noun")
        adjective = request.args.getlist("adjective")

    template = choice(MADLIB_TEMPLATES)
    return render_template(template,
                            person=person,
                            color=color,
                            noun=noun,
                            adjective=adjective)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True, port=5000)
