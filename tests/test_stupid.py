
import unittest

from doctest_travis import *

class TestStupidFunctions(unittest.TestCase):

	def test_stupid_sum(self):
		self.assertEqual(stupid_sum(1,2), 4)

	def test_stupid_mul(self):
		self.assertEqual(stupid_mul(2,2), 8)
