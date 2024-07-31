#!/usr/bin/python3

"""flask routing module"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """home route for home page or root page"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route for hbnb page"""

    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
