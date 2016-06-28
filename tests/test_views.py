# ----- Imports ----- #

import unittest
import around_the_house


# ----- Tests ----- #

class TestViews(unittest.TestCase):

	"""Tests the views, the core of the flask app."""

	def setUp(self):

		around_the_house.app.config['TESTING'] = True
		self.app = around_the_house.app.test_client()

	def test_home_route(self):

		"""Makes sure the homepage is retrieved correctly."""

		result = self.app.get('/')
		self.assertEqual(result.status, '200 OK')
