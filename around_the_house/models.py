# ----- Imports ----- #

from tinydb import TinyDB, Query
import re


# ----- Setup ----- #

DB_FILE = 'db.json'

db = TinyDB(DB_FILE)
Item = Query()


# ----- Model Functions ----- #

def item(id):

	"""Retrieves an item with a given id."""

	item_data = db.get(eid=int(id))

	if item_data:
		item_data['id'] = item_data.eid

	return item_data


def search(terms):

	"""Searches and returns all items matching given search terms."""

	query = lambda s: re.search(terms, s, re.IGNORECASE)
	result = db.search(Item.title.test(query) | Item.author.test(query))

	for record in result:
		record['id'] = record.eid

	return result


def new_item(item_data):

	"""Adds a new item to the database and returns its id."""

	print(item_data)
	return db.insert(item_data)


def edit(item_data):

	"""Updates the data on a given item by id."""

	id = int(item_data['id'])
	item_data.pop('id', None)

	db.update(item_data, eids=[id])


def delete(id):

	"""Deletes an item by id."""

	db.remove(eids=[int(id)])
