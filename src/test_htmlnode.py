import unittest
from htmlnode import HTMLNode

test_props1 = {
				"href": "https://www.google.com",
				"target": "_blank",
			  }
test_props2 = {
				"href": "https://www.google.com",
				"target": "_blank",
				"test": "test_test",
			  }

class TestHTMLNode(unittest.TestCase):
	def test_eq_props2html(self):
		node = HTMLNode(
			props=test_props1
			)
		self.assertEqual(
			' href="https://www.google.com" target="_blank"', 
			node.props_to_html()
			)

	def test_eq_props2html2(self):
		node = HTMLNode(
			props=test_props2
			)
		self.assertEqual(
			' href="https://www.google.com" target="_blank" test="test_test"', 
			node.props_to_html()
			)

	def test_noteq_props2html(self):
		node = HTMLNode(
			props=test_props1
			)
		node2 = HTMLNode(
			props=test_props2
			)
		self.assertNotEqual(
			node.props_to_html(), 
			node2.props_to_html()
			)

	def test_no_props(self):
		node = HTMLNode(
			tag='p',
			value='hello'
			)
		self.assertEqual(
			node.props_to_html(),
			""
			)

	def test_repr(self):
		node = HTMLNode(
			tag='p',
			value='hello'
			)
		self.assertEqual(
			"HTMLNode(p,hello,None,None)",
			repr(node)
			)

if __name__ == '__main__':
	unittest.main()
