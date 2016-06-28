# ----- Imports ----- #

import unittest
import json
import around_the_house


# ----- Functions ----- #

def post_mock(app, entry={'dummy': 'entry'}):

	"""Posts a dummy entry to the app."""

	return app.post('/new_item',
		data=json.dumps(entry),
		content_type='application/json')


# ----- Tests ----- #

class TestViews(unittest.TestCase):

	"""Tests the views, the core of the flask app."""

	def setUp(self):

		around_the_house.app.config['TESTING'] = True
		self.app = around_the_house.app.test_client()
		around_the_house.models.db = around_the_house.models.TinyDB('test.json')
		self.db = around_the_house.models.db

	def tearDown(self):

		self.db.purge_tables()

	def test_home_route(self):

		"""Makes sure the homepage is retrieved correctly."""

		result = self.app.get('/')
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.mimetype, 'text/html')

	def test_new_item(self):

		"""Checks that the new item page is returned."""

		result = self.app.get('/new_item')
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.mimetype, 'text/html')

	def test_new_item_added(self):

		"""Checks that an item is added."""

		item = {'dummy': 'entry'}
		result = post_mock(self.app, item)

		self.assertEqual(result.status_code, 201)
		self.assertEqual(result.mimetype, 'text/html')

		self.assertEqual(self.db.get(eid=1), item)

	def test_item(self):

		"""Checks that an item is retrieved."""

		result = post_mock(self.app)

		result = self.app.get('/item/1')
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.mimetype, 'text/html')

	def test_no_item(self):

		"""Checks that an error is raised when item does not exist."""

		result = self.app.get('/item/1')
		self.assertEqual(result.status_code, 404)

	def test_search(self):

		"""Checks that search returns a response HTML page."""

		result = self.app.get('/search?terms=dummy')
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.mimetype, 'text/html')

	def test_edit_page(self):

		"""Makes sure the edit page is sent on GET."""

		post_mock(self.app)

		result = self.app.get('/edit/1')
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.mimetype, 'text/html')

	def test_edit_no_item(self):

		"""Checks that an error is raised when item does not exist."""

		result = self.app.get('/edit/1')
		self.assertEqual(result.status_code, 404)

	def test_edit_put(self):

		"""Makes sure an item is edited correctly."""

		post_mock(self.app)
		new_entry = {'dummy': 'another_entry'}

		result = self.app.put('/edit/1',
			data=json.dumps(new_entry),
			content_type='application/json')

		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.mimetype, 'text/html')

		self.assertEqual(self.db.get(eid=1), new_entry)

	def test_delete(self):

		"""Checks that an item is deleted."""

		post_mock(self.app)
		result = self.app.delete('/delete/1')

		self.assertEqual(result.status_code, 204)
		self.assertEqual(result.mimetype, 'text/html')

		result = self.app.get('/item/1')
		self.assertEqual(result.status_code, 404)
		self.assertEqual(self.db.get(eid=1), None)
