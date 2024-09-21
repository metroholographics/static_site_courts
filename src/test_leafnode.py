import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
	def test_init(self):
		node = LeafNode(
			"p",
			"This is a paragraph of text.",
			)
		self.assertEqual(
			node.tag,
			"p")
		self.assertEqual(
			node.value,
			"This is a paragraph of text.")
		self.assertEqual(
			node.children,
			None,
			)
		self.assertEqual(
			node.props,
			None,
			)
	def test_init2(self):
		node = LeafNode(
			"a",
			"Paragraph of text.",
			{"class": "greeting", "href": "www.google.com"}
			)
		self.assertEqual(
			node.tag,
			"a",
			)
		self.assertEqual(
			node.value,
			"Paragraph of text.",
			)
		self.assertEqual(
			node.children,
			None,
			)
		self.assertEqual(
			node.props,
			{"class": "greeting", "href": "www.google.com"},
			)

	def test_check_if_value(self):
		node = LeafNode(
			"p",
			None,
			{"class": "greeting"},
			)
		self.assertRaises(ValueError, node.to_html)

	def test_check_to_html(self):
		node = LeafNode(
			"p",
			"This is a paragraph of text.",
			)
		self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

		node2 = LeafNode(
			None,
			"This is a paragraph of text.",
			)
		self.assertEqual(node2.to_html(), "This is a paragraph of text.")

		node3 = LeafNode(
			"a",
			"Click me!",
			{"href": "https://www.google.com"},
			)
		self.assertEqual(node3.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == '__main__':
	unittest.main()









