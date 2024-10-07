import unittest

from generator import *

class TestGenerator(unittest.TestCase):
	def test_extract_title(self):
		self.assertEqual(extract_title("# Hello"), "Hello")
		self.assertEqual(extract_title("# Hello  "), "Hello")
		self.assertRaises(Exception, extract_title, "Hello\n* no title\n*## Hello")
