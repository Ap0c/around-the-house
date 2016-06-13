# ----- Imports ----- #

import unittest
import book_db.models as models


# ----- Functions ----- #

def mock_book(title='Book One', author='Author One', location='Location One'):

	"""Creates a mocked book in the database."""

	return models.new_book(title, author, location), title, author, location


# ----- Tests ----- #

class TestModels(unittest.TestCase):

	"""Tests the model methods."""

	def setUp(self):

		models.db = models.Database('test.db', models.DB_SCHEMA)

	def tearDown(self):

		models.db.query('DELETE FROM books')

	def test_new_book(self):

		"""Checks if a book is added to the database."""

		book_id = mock_book()[0]
		self.assertEqual(book_id, 1)

	def test_retrieve_book(self):

		"""Checks if a book is correctly retrieved from the database."""

		book_id, title, author, location = mock_book()
		book = models.book(book_id)

		self.assertIsNotNone(book)
		self.assertEqual(book['docid'], book_id)
		self.assertEqual(book['title'], title)
		self.assertEqual(book['author'], author)
		self.assertEqual(book['location'], location)

	def test_retrieve_no_book(self):

		"""Checks if a book is not retrieved from the database."""

		book = models.book(1)
		self.assertIsNone(book)

	def test_search_title(self):

		"""Makes sure search returns title results."""

		book_id = mock_book(title='Dummy Title', author='Made Up Author')[0]

		book = models.search('Dummy')[0]
		self.assertEqual(book['docid'], book_id)

	def test_search_author(self):

		"""Makes sure search returns author results."""

		book_id = mock_book(title='Dummy Title', author='Made Up Author')[0]

		book = models.search('Made')[0]
		self.assertEqual(book['docid'], book_id)

