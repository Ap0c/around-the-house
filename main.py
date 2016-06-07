# ----- Imports ----- #

from flask import Flask


# ----- Setup ----- #

# The flask app object.
app = Flask(__name__)


# ----- Routes ----- #

@app.route('/')
def home():
	return 'Hello world'


@app.route('/<id>')
def book(id):

	return "Hello, I'm a book with the id {}".format(id)


# ----- Run ----- #

if __name__ == '__main__':
	app.run(debug=True)
