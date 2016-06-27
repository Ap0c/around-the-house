# ----- Imports ----- #

from tinydb import TinyDB, Query
import re


# ----- Setup ----- #

DB_FILE = 'db.json'

db = TinyDB(DB_FILE)
Book = Query()


# ----- Model Functions ----- #

def book(id):

	"""Retrieves a book with given id."""

	return db.get(eid=int(id))


def search(terms):

	"""Searches and returns all books matching given search terms."""

	find_terms = lambda s: re.search(terms, s, re.IGNORECASE)

	return db.search(Book.title.test(find_terms) | Book.author.test(find_terms))


def new_book(title, author, location):

	"""Adds a new book to the database and returns its id."""

	return db.insert({'title': title, 'author': author, 'location': location})


def edit(id, title, author, location):

	"""Updates the data on a given book by id."""

	db.update({'title': title, 'author': author, 'location': location},
		eids=[id])


def delete(id):

	"""Deletes a book by id."""

	db.remove(eids=[id])
