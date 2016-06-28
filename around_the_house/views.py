# ----- Imports ----- #

from flask import render_template, abort, request

from around_the_house import app
import around_the_house.models as models


# ----- Routes ----- #

@app.route('/')
def home():

	"""The main page, search-oriented."""

	return render_template('main.html')


@app.route('/search')
def search():

	"""Retrieves html fragment of search results."""

	terms = request.args.get('terms')
	items = models.search(terms)

	return render_template('list.html', items=items)


@app.route('/item/<int:id>')
def item(id):

	"""Displays information about a item with a given id."""

	item_data = models.item(id)

	if item_data:
		return render_template('item.html', **item_data)
	else:
		abort(404)


@app.route('/new_item', methods=['GET', 'POST'])
def new_item():

	"""Allows the user to add a new item."""

	if request.method == 'GET':
		return render_template('new_item.html')
	elif request.method == 'POST':

		fields = request.get_json()
		item_id = models.new_item(fields)

		return str(item_id), 201


@app.route('/edit/<int:id>', methods=['GET', 'PUT'])
def edit(id):

	"""Allows the user to edit a specific item."""

	if request.method == 'GET':

		item_data = models.item(id)

		if item_data:
			return render_template('edit.html', **item_data)
		else:
			abort(404)

	elif request.method == 'PUT':

		fields = request.get_json()
		models.edit(id, fields)

		return str(id), 200


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):

	"""Deletes a given item by id."""

	models.delete(id)

	return '', 204
