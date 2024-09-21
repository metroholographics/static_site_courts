class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError('to_html method not implemented')

	def props_to_html(self):
		if self.props is None:
			return ''
		prop_str = list(
			map(
				lambda x: f' {x}="{self.props[x]}"',
				self.props
				)
			)
		return ''.join(prop_str)

	def __repr__(self):
		return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("Invalid HTML: no value")
		if self.tag is None:
			return self.value

		prop_str = self.props_to_html()

		return f'<{self.tag}{prop_str}>{self.value}</{self.tag}>'

	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"