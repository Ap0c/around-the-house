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

def book(id):

	"""Retrieves a book with given id."""

	query = 'SELECT docid, title, author, location FROM books WHERE docid=?'
	book_data = db.query(query, id)

	if len(book_data) > 0:
		return book_data[0]
	else:
		return None
