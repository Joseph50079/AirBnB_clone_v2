#!/usr/bin/python3

"""flask routing module"""

from flask import Flask, abort, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """home route for home page or root page"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route for hbnb page"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """C_text route for dynamic text page"""

    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """python_text route for dynamic text page"""

    return f"Python {escape(text).replace('_', ' ')}"


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """
    n route for dynamic text page when n is an integer

    """
    try:
        num = int(n)

        return f"{escape(n).replace('_', ' ')} is a number"
    except ValueError:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """
    n route for dynamic text page when n is an integer

    """
    try:
        num = int(n)

        return render_template(
            '5-number.html', title='HBNB', message=f"Number: {num}")
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
