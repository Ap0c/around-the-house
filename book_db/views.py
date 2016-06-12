# ----- Imports ----- #

from flask import render_template, abort, request

from book_db import app
from .db import Database
import book_db.models as models

db = models.db


# ----- Routes ----- #

@app.route('/')
def home():

	"""The main page, search-oriented."""

	return render_template('main.html')


@app.route('/search')
def search():

	"""Retrieves html fragment of search results."""

	terms = request.args.get('terms')
	books = models.search(terms)

	return render_template('list.html', books=books)


@app.route('/book/<id>')
def book(id):

	"""Displays information about a book with a given id."""

	book_data = models.book(id)

	if book_data:
		return render_template('book.html', **book_data)
	else:
		abort(404)


@app.route('/new_book', methods=['GET', 'POST'])
def new_book():

	"""Allows the user to add a new book."""

	if request.method == 'GET':
		return render_template('new_book.html')
	elif request.method == 'POST':

		fields = [request.args.get(f) for f in ('title', 'author', 'location')]
		book_id = models.new_book(*fields)

		return str(book_id), 201


@app.route('/edit/<id>', methods=['GET', 'PUT'])
def edit(id):

	"""Allows the user to edit a specific book."""

	if request.method == 'GET':

		book_data = db.query("""SELECT docid, title, author, location FROM books
			WHERE docid = ?""", id)

		if len(book_data) > 0:
			return render_template('edit.html', **book_data[0])
		else:
			abort(404)

	elif request.method == 'PUT':

		req_args = request.args

		query = 'UPDATE books SET title=?, author=?, location=? WHERE docid=?'
		args = [req_args.get(f) for f in ('title', 'author', 'location')]
		args.append(id)
		db.query(query, tuple(args))

		return id, 200
