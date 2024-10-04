import unittest

from inline_markdown import *


class TestTexttoTextNodes(unittest.TestCase):
	def test_text_to_text_nodes(self):
		nodes = text_to_textnodes(
			"This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		)
		self.assertListEqual(
			[
				TextNode("This is ", t_t_text),
				TextNode("text", t_t_bold),
				TextNode(" with an ", t_t_text),
				TextNode("italic", t_t_italic),
				TextNode(" word and a ", t_t_text),
				TextNode("code block", t_t_code),
				TextNode(" and an ", t_t_text),
				TextNode("obi wan image", t_t_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
				TextNode(" and a ", t_t_text),
				TextNode("link", t_t_link, "https://boot.dev"),
			],
			nodes
		)


class TestSplitNodesDelimiter(unittest.TestCase):
	def test_all_delimiters(self):
		node = TextNode("This is text with a `code block` word", t_t_text)

		self.assertEqual(
			split_nodes_delimiter([node], "`", t_t_code),
			[
			    TextNode("This is text with a ", t_t_text),
			    TextNode("code block", t_t_code),
			    TextNode(" word", t_t_text),
			]
		)

		node = TextNode("*italic block* text in this node", t_t_text)

		self.assertEqual(
			split_nodes_delimiter([node], "*", t_t_italic),
			[
			    TextNode("italic block", t_t_italic),
			    TextNode(" text in this node", t_t_text),
			]
		)

	def test_multiple_delimiters(self):
		node = TextNode("This is `1 code block` and another `code block`", t_t_text)
		self.assertEqual(
			split_nodes_delimiter([node], "`", t_t_code),
			[
			    TextNode("This is ", t_t_text),
			    TextNode("1 code block", t_t_code),
			    TextNode(" and another ", t_t_text),
			    TextNode("code block", t_t_code),
			]
		)

class TestExtractImagesandText(unittest.TestCase):
	def test_extract_images(self):
		text = "This is [a link](http://example.com) and this is ![an image](http://example.com/image.jpg)"
		self.assertEqual(extract_markdown_images(text),
			[('an image', 'http://example.com/image.jpg')])

		text = "![an image](http://example.com/image.jpg)"
		self.assertEqual(extract_markdown_images(text),
			[('an image', 'http://example.com/image.jpg')])

	def test_extract_links(self):
		text = "This is [a link](http://example.com) and another link [an image](http://example.com/image.jpg)"
		self.assertEqual(extract_markdown_links(text),
			[('a link', 'http://example.com'), ('an image', 'http://example.com/image.jpg')])

		text = "[a link](http://example.com)"
		self.assertEqual(extract_markdown_links(text),
			[('a link', 'http://example.com')])

class TestSplitNodesImagesLinks(unittest.TestCase):
	def test_split_images(self):
		node = [
					TextNode(
						"This is an image ![cat](www.cat.com)",
						t_t_text,
					),
					TextNode(
						"This is an image ![dog](www.dog.com) in the middle",
						t_t_text,
					)
				]

		self.assertListEqual(
			split_nodes_image(node),
				[
					TextNode("This is an image ",t_t_text), TextNode("cat", t_t_image,'www.cat.com'),
					TextNode("This is an image ",t_t_text), TextNode("dog", t_t_image,'www.dog.com'),
					TextNode(" in the middle", t_t_text),
				]
			)
	def test_split_links(self):
		node = [
			TextNode(
				"This is a link [cat site](www.cat.com)",
				t_t_text,
			),
			TextNode(
				"This is a link [dog site](www.dog.com) in the middle",
				t_t_text,
			)
		]

		self.assertListEqual(
			split_nodes_link(node),
				[
					TextNode("This is a link ",t_t_text), TextNode("cat site", t_t_link,'www.cat.com'),
					TextNode("This is a link ",t_t_text), TextNode("dog site", t_t_link,'www.dog.com'),
					TextNode(" in the middle", t_t_text),
				]
			)
		
if __name__ == '__main__':
	unittest.main()
