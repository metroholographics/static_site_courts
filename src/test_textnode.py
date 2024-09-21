import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode('This is a text node', 'bold')
		node2 = TextNode('This is a text node', 'bold')
		self.assertEqual(node, node2)

	def test_eq_url(self):
		node = TextNode('Test', 'italic', 'www.google.com')
		node2 = TextNode('Test', 'italic', 'www.google.com')
		self.assertEqual(node, node2)

	def test_not_eq(self):
		node = TextNode('Test', 'italic', 'www.google.com')
		node2 = TextNode('Test', 'italics', 'www.google.com')
		self.assertNotEqual(node, node2)

	def test_not_eq_url(self):
		node = TextNode('Test', 'italic', 'www.google.com')
		node2 = TextNode('Test', 'italic', 'www.facebook.com')
		self.assertNotEqual(node, node2)

	def test_repr(self):
		node = TextNode('Test', 'italic')
		self.assertEqual("TextNode(Test, italic, None)", repr(node))


if __name__ == '__main__':
	unittest.main()