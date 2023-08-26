from flask import Flask
"""Flask model to use flask framework
"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnt():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
