from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *

def main():
	text = """
# This is a heading

## This is a heading with **bolded text**

This paragraph has an [image](www.google.com)

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

1. This is the first list item in a list block
2. This is a different list item
3. This is another list item
	"""

	code_text = """
# This is a heading

```push()```

a normal paragraph

>quote block this is a quote
>from someone
	"""

	tag = markdown_to_html_node(text)

	print(tag.to_html())

if __name__ == "__main__":
	main()