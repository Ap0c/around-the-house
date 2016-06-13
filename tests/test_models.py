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

		book_id = models.new_book('Book One', 'Author One', 'Location One')
		self.assertEqual(book_id, 1)

