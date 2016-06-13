# ----- Imports ----- #

import unittest
import book_db.models as models


# ----- Tests ----- #

class TestModels(unittest.TestCase):

	"""Tests the model methods."""

	def setUp(self):

		models.db = models.Database('test.db', models.DB_SCHEMA)

	def tearDown(self):

		models.db.query('DELETE FROM books')

	def test_new_book(self):

		"""Checks if a book is added to the database."""

		book_id = models.new_book('Book One', 'Author One', 'Location One')
		self.assertEqual(book_id, 1)

	def test_retrieve_book(self):

		"""Checks if a book is correctly retrieved from the database."""

		title, author, location = 'Book One', 'Author One', 'Location One'

		models.new_book(title, author, location)
		book = models.book(1)

		self.assertIsNotNone(book)
		self.assertEqual(book['docid'], 1)
		self.assertEqual(book['title'], title)
		self.assertEqual(book['author'], author)
		self.assertEqual(book['location'], location)

	def test_retrieve_no_book(self):

		"""Checks if a book is not retrieved from the database."""

		book = models.book(1)
		self.assertIsNone(book)
