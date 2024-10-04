from htmlnode import LeafNode

t_t_text = "text"
t_t_bold = "bold"
t_t_italic = "italic"
t_t_code = "code"
t_t_link = "link"
t_t_image = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other_text_node):
		if (self.text == other_text_node.text and 
			self.text_type == other_text_node.text_type and 
			self.url == other_text_node.url):

			return True

		return False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
	match text_node.text_type:
		case "text":
			return LeafNode(None, text_node.text)
		case "bold":
			return LeafNode('b', text_node.text)
		case "italic":
			return LeafNode('i', text_node.text)
		case "code":
			return LeafNode('code', text_node.text)
		case "link":
			return LeafNode('a', text_node.text,
							{"href": text_node.url},
					)
		case "image":
			return LeafNode('img', "",
							{"src": text_node.url, "alt": text_node.text},
					)
		case _:
			raise ValueError(f"Invalid text_type {text_node.text_type}")
