import unittest

from textnode import *


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

class TestTextNodeToHTMLNode(unittest.TestCase):
	def test_text(self):
		test = TextNode("raw text", "text")
		self.assertEqual(repr(text_node_to_html_node(test)),
			"LeafNode(None, raw text, None)")
		test = TextNode("bold text", "bold")
		self.assertEqual(repr(text_node_to_html_node(test)),
			"LeafNode(b, bold text, None)")

	def test_link_and_image(self):
		test = text_node_to_html_node(TextNode(
				"Click this link!",
				"link",
				"www.google.com",
				)
		)

		self.assertEqual(test.to_html(),
			'<a href="www.google.com">Click this link!</a>'
		)

		test = text_node_to_html_node(TextNode(
				"dog smiling",
				"image",
				"/images/dog-smiling.png",
				)
		)
		self.assertEqual(test.to_html(),
			'<img src="/images/dog-smiling.png" alt="dog smiling"></img>'
		)


