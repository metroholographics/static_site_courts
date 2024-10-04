import unittest
from htmlnode import LeafNode, ParentNode

class TestLeaf_Parent_Node(unittest.TestCase):
	def test_check_if_value(self):
		node = LeafNode(
			"p",
			None,
			{"class": "greeting"},
			)
		self.assertRaises(ValueError, node.to_html)

	def test_check_to_html(self):
		node = LeafNode("p", "This is a paragraph of text.")
		self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

		node2 = LeafNode(None,"This is a paragraph of text.")
		self.assertEqual(node2.to_html(), "This is a paragraph of text.")

		node3 = LeafNode(
			"a",
			"Click me!",
			{"href": "https://www.google.com"},
			)
		self.assertEqual(node3.to_html(),
			'<a href="https://www.google.com">Click me!</a>'
			)

	def test_parent(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)

		self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
				LeafNode("a","Click this link!",{"href": "www.google.com"})
			],
		)

		self.assertEqual(
			'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a href="www.google.com">Click this link!</a></p>',
			node.to_html()
		)

	def test_nestedparent(self):
		node = ParentNode(
			"p",
			[
				ParentNode(
					"h2",
					[
						LeafNode("b", "Bold text"),
						LeafNode(None, "Normal text"),
					],
				),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)

		self.assertEqual("<p><h2><b>Bold text</b>Normal text</h2><i>italic text</i>Normal text</p>",
			node.to_html()
		)

	def test_parent_no_children(self):
		node = ParentNode(
			"p",
			None,
		)
		self.assertRaises(ValueError, node.to_html)

		node = ParentNode(
			"p",
			[""],
		)
		self.assertEqual("<p></p>", node.to_html())


if __name__ == '__main__':
	unittest.main()









