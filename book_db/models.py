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

	book_data = db.get(eid=int(id))
	book_data['id'] = book_data.eid

	return book_data


def search(terms):

	"""Searches and returns all books matching given search terms."""

	query = lambda s: re.search(terms, s, re.IGNORECASE)
	result = db.search(Book.title.test(query) | Book.author.test(query))

	for item in result:
		item['id'] = item.eid

	return result


def new_book(title, author, location):

	"""Adds a new book to the database and returns its id."""

	return db.insert({'title': title, 'author': author, 'location': location})


def edit(id, title, author, location):

	"""Updates the data on a given book by id."""

	db.update({'title': title, 'author': author, 'location': location},
		eids=[int(id)])


def delete(id):

	"""Deletes a book by id."""

	db.remove(eids=[int(id)])
