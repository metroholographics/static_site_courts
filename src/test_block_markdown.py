import unittest
from block_markdown import *

class TestMarkdownToBlock(unittest.TestCase):
	def test_markdown_to_blocks(self):
		text = "# This is a heading  \n\nThis is a paragraph\n\n \n* First list\n* Second list\n* Third list"
		self.assertListEqual(
			markdown_to_blocks(text),
			[
				"# This is a heading",
				"This is a paragraph",
				"* First list\n* Second list\n* Third list"
			]
		)

class TestBlockToBlockType(unittest.TestCase):
	def test_heading(self):
		self.assertEqual('heading', block_to_block_type('# Heading'))
		self.assertEqual('heading', block_to_block_type('### Heading'))
		self.assertEqual('heading', block_to_block_type('###### Heading'))
		self.assertEqual('paragraph', block_to_block_type('####### Heading'))
		self.assertEqual('paragraph', block_to_block_type('###Heading'))

	def test_code(self):
		self.assertEqual('code', block_to_block_type('```\nThis is code\n```'))
		self.assertNotEqual('code', block_to_block_type("```\nThis isnt't code\n``"))
		self.assertNotEqual('code', block_to_block_type("This isn't code\n```"))
		self.assertEqual('paragraph', block_to_block_type("```\nThis isnt't code\n``"))

	def test_quote(self):
		self.assertEqual('quote', block_to_block_type('>This is a quote'))
		self.assertEqual('quote', block_to_block_type('> This is a quote'))
		self.assertEqual('paragraph', block_to_block_type("< This isn't a quote"))

	def test_unordered_list(self):
		self.assertEqual('unordered_list', block_to_block_type("* This\n* is\n* a\n* list"))
		self.assertEqual('unordered_list', block_to_block_type("- This\n- is\n- a\n- list"))
		self.assertEqual('unordered_list', block_to_block_type("- This\n* is\n- a\n* list"))
		self.assertEqual('paragraph', block_to_block_type("- This\n isn't\n- a\n* list"))
		self.assertEqual('paragraph', block_to_block_type("- This\n- isn't\n- a\n> list"))

	def test_ordered_list(self):
		self.assertEqual('ordered_list', block_to_block_type("1. This\n2. is\n3. a\n4. list"))
		self.assertEqual('paragraph', block_to_block_type("1. This\n2. isn't\n4. a\n3. list"))
		self.assertEqual('paragraph', block_to_block_type("1. This\n1. isn't\n4. a\n3. list"))
		self.assertEqual('paragraph', block_to_block_type("2. This\n3. isn't\n4. a\n5. list"))

class TestMarkdownToHTMLNode(unittest.TestCase):
	def test_markdown_to_html_node(self):
		text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

1. This is the first list item in a list block
2. This is a list item
3. This is another list item
"""
		node = "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ol><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ol></div>"
		self.assertEqual(markdown_to_html_node(text).to_html(), node)

		text = """
> This is a
> blockquote block
"""
		node = "<div><blockquote>This is a blockquote block</blockquote></div>"
		self.assertEqual(markdown_to_html_node(text).to_html(), node)

		


