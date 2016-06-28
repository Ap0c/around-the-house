# ----- Imports ----- #

import unittest
import around_the_house.models as models


# ----- Functions ----- #

def mock_item(title='Item One', author='Author One', location='Location One'):

	"""Creates a mocked item in the database."""

	item_data = {'title': title, 'author': author, 'location': location}

	return models.new_item(item_data), title, author, location


# ----- Tests ----- #

class TestModels(unittest.TestCase):

	"""Tests the model methods."""

	def setUp(self):

		models.db = models.TinyDB('test.json')

	def tearDown(self):

		models.db.purge_tables()

	def test_new_item(self):

		"""Checks if an item is added to the database."""

		item_id = mock_item()[0]
		self.assertEqual(item_id, 1)

	def test_retrieve_item(self):

		"""Checks if an item is correctly retrieved from the database."""

		item_id, title, author, location = mock_item()
		item = models.item(item_id)

		self.assertIsNotNone(item)
		self.assertEqual(item['id'], item_id)
		self.assertEqual(item['title'], title)
		self.assertEqual(item['author'], author)
		self.assertEqual(item['location'], location)

	def test_retrieve_no_item(self):

		"""Checks if an item is not retrieved from the database."""

		item = models.item(1)
		self.assertIsNone(item)

	def test_search_title(self):

		"""Makes sure search returns title results."""

		item_id = mock_item(title='Dummy Title', author='Made Up Author')[0]

		item = models.search('Dummy')[0]
		self.assertEqual(item['id'], item_id)

	def test_search_author(self):

		"""Makes sure search returns author results."""

		item_id = mock_item(title='Dummy Title', author='Made Up Author')[0]

		item = models.search('Made')[0]
		self.assertEqual(item['id'], item_id)

	def test_edit(self):

		"""Makes sure an item is edited correctly."""

		item_id = mock_item()[0]

		item_data = {'title': 'Item Two', 'author': 'Author Two',
			'location': 'Location Two'}
		models.edit(item_id, item_data)

		item = models.item(item_id)

		self.assertEqual(item['title'], item_data['title'])
		self.assertEqual(item['author'], item_data['author'])
		self.assertEqual(item['location'], item_data['location'])

	def test_delete(self):

		"""Checks an item is deleted correctly."""

		item_id = mock_item()[0]
		models.delete(item_id)

		item = models.item(item_id)
		self.assertIsNone(item)
