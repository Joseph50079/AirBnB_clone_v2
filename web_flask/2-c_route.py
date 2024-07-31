#!/usr/bin/python3

"""flask routing module"""

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
