# ----- Imports ----- #

import os.path

from .db import Database


# ----- Setup ----- #

# The database schema file.
DB_SCHEMA = os.path.join(os.path.dirname(os.path.realpath(__file__)),
	'schema.sql')

# The database file.
DB_FILE = 'books.db'

# Handles database connections and queries.
db = Database(DB_FILE, DB_SCHEMA)


# ----- Model Functions ----- #

def change_db(new_db):

	"""Changes the default database file based on given path, for testing."""

	global db
	db = Database(new_db, DB_SCHEMA)


def book(id):

	"""Retrieves a book with given id."""

	query = 'SELECT docid, title, author, location FROM books WHERE docid=?'
	book_data = db.query(query, (id,))

	if len(book_data) > 0:
		return book_data[0]
	else:
		return None


def search(terms):

	"""Searches and returns all books matching given search terms."""

	matchstring = 'title:*{0}* OR author:*{0}*'.format(terms)
	query = 'SELECT docid, * FROM books WHERE books MATCH ?'

	return db.query(query, (matchstring,))


def new_book(title, author, location):

	"""Adds a new book to the database and returns its id."""

	query = 'INSERT INTO books (title, author, location) VALUES (?, ?, ?)'

	return db.query(query, (title, author, location))


def edit(id, title, author, location):

	"""Updates the data on a given book by id."""

	query = 'UPDATE books SET title=?, author=?, location=? WHERE docid=?'

	db.query(query, (title, author, location, id))


def delete(id):

	"""Deletes a book by id."""

	db.query('DELETE FROM books WHERE docid=?', (id,))
