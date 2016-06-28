# ----- Imports ----- #

import unittest
import json
import around_the_house


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

	def test_new_item(self):

		"""Checks that the new item page is returned."""

		result = self.app.get('/new_item')
		self.assertEqual(result.status_code, 200)

	def test_new_item_added(self):

		"""Checks that an item is added."""

		result = self.app.post('/new_item',
			data=json.dumps({'dummy': 'entry'}),
			content_type='application/json')

		self.assertEqual(result.status_code, 201)
		self.assertEqual(result.mimetype, 'text/html')

	def test_item(self):

		"""Checks that an item is retrieved."""

		result = self.app.post('/new_item',
			data=json.dumps({'dummy': 'entry'}),
			content_type='application/json')

		result = self.app.get('/item/1')
		self.assertEqual(result.status_code, 200)

	def test_no_item(self):

		"""Checks that an error is raised when item does not exist."""

		result = self.app.get('/item/1')
		self.assertEqual(result.status_code, 404)
