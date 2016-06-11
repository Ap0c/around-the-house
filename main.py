# ----- Imports ----- #

from flask import Flask, render_template, abort, request
import os.path
from db import Database


# ----- Setup ----- #

# The database schema file.
DB_SCHEMA = os.path.join(os.path.dirname(os.path.realpath(__file__)),
	'schema.sql')

# The database file.
DB_FILE = 'books.db'

# The flask app object.
app = Flask(__name__)

# Handles database connections and queries.
db = Database(DB_FILE, DB_SCHEMA)


# ----- Routes ----- #

@app.route('/')
def home():

	"""The main page, search-oriented."""

	return render_template('main.html')


@app.route('/search')
def search():

	"""Retrieves html fragment of search results."""

	terms = request.args.get('terms')
	matchstring = 'title:{} OR author:{}'.format(terms, terms)
	query = """SELECT docid, title, author, location FROM books
		WHERE books MATCH ?"""

	results = db.query(query, (matchstring,))

	return render_template('list.html', books=results)


@app.route('/book/<id>')
def book(id):

	"""Displays information about a book with a given id."""

	book_data = db.query('SELECT * FROM books WHERE docid = ?', id)

	if len(book_data) > 0:
		return render_template('book.html', **book_data[0])
	else:
		abort(404)


@app.route('/new_book', methods=['GET', 'POST'])
def new_book():

	"""Allows the user to add a new book."""

	if request.method == 'GET':
		return render_template('new_book.html')
	elif request.method == 'POST':

		query = 'INSERT INTO books (title, author, location) VALUES (?, ?, ?)'
		args = [request.args.get(f) for f in ('title', 'author', 'location')]
		id = db.query(query, tuple(args))

	return str(id), 201


@app.route('/edit/<id>')
def edit(id):

	"""Allows the user to edit a specific book."""

	book_data = db.query("""SELECT docid, title, author, location FROM books
		WHERE docid = ?""", id)

	if len(book_data) > 0:
		return render_template('edit.html', **book_data[0])
	else:
		abort(404)


# ----- Run ----- #

if __name__ == '__main__':
	app.run(debug=True)
