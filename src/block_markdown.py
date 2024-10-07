from htmlnode import *
from inline_markdown import *
from textnode import *

paragraph_block = 'paragraph'
heading_block = 'heading'
code_block = 'code'
quote_block = 'quote'
olist_block = 'ordered_list'
ulist_block = 'unordered_list'

def markdown_to_blocks(markdown):
	block_list = []
	markdown_split = markdown.split('\n\n')
	for split in markdown_split:
		text_clean = split.strip()
		if text_clean != '':
			block_list.append(text_clean)
	return block_list

def block_to_block_type(block):
	if block.startswith(('# ','## ','### ','#### ','##### ','###### ')):
		return heading_block
	if block.startswith('```') and block.endswith('```'):
		return code_block
	list_blocks = block.split('\n')
	if list_blocks == [line for line in list_blocks if line.startswith('>')]:
		return quote_block
	if list_blocks == [line for line in list_blocks if line.startswith('* ') or line.startswith('- ')]:
		return ulist_block
	if list_blocks[0].startswith('1. '):
		valid = True
		next_count = 1
		for line in list_blocks:
			if not line.startswith(f'{next_count}. '):
				valid = False
				break
			next_count += 1
		if valid:
			return olist_block
	return paragraph_block

def markdown_to_html_node(markdown):
	main_children = []
	block_list = markdown_to_blocks(markdown)
	for block in block_list:
		blocktype = block_to_block_type(block)
		block_tag = block_type_to_html_tag(block, blocktype)
		if blocktype == olist_block:
			block_children = handle_olist_block(block)
		elif blocktype == ulist_block:
			block_children = handle_ulist_block(block)
		elif blocktype == code_block:
			block_children = handle_code_block(block)
		elif blocktype == quote_block:
			block_children = handle_quote_block(block)
		elif blocktype == heading_block:
			block_children = handle_heading_block(block)
		elif blocktype == paragraph_block:
			block_children = handle_paragraph_block(block)

		block_html_node = ParentNode(block_tag, block_children)
		main_children.append(block_html_node)
	return ParentNode('div', main_children)

def handle_olist_block(block):
	splits = block.split('\n')
	block_html_nodes = []
	for i in range(len(splits)):
		line_html = HTMLNode('li')
		text = get_block_text(splits[i], f'{i + 1}. ')
		text_nodes = text_to_textnodes(text)
		child_nodes = []
		for node in text_nodes:
			child_nodes.append(text_node_to_html_node(node))
		line_html = ParentNode('li', child_nodes)
		block_html_nodes.append(line_html)
	return block_html_nodes

def handle_ulist_block(block):
	splits = block.split('\n')
	block_html_nodes = []
	for split in splits:
		text = split[2:] #get_block_text(split, '*- ')
		text_nodes = text_to_textnodes(text)
		child_nodes = []
		for node in text_nodes:
			child_nodes.append(text_node_to_html_node(node))
		line_html = ParentNode('li', child_nodes)
		block_html_nodes.append(line_html)
	return block_html_nodes

def handle_code_block(block):
	block_html_nodes = []
	text = get_block_text(block, '```')
	text_nodes = text_to_textnodes(text)
	code_children = []
	for node in text_nodes:
		code_children.append(text_node_to_html_node(node))
	code_html = ParentNode('code', code_children)
	block_html_nodes.append(code_html)
	return block_html_nodes

def handle_quote_block(block):
	block_html_nodes = []
	splits = block.split('\n')
	quote_lines = []
	for split in splits:
		text = get_block_text(split, '>').strip()
		quote_lines.append(text)
	text = " ".join(quote_lines)
	text_nodes = text_to_textnodes(text)
	for node in text_nodes:
		block_html_nodes.append(text_node_to_html_node(node))
	return block_html_nodes

def handle_heading_block(block):
	text = get_block_text(block, '# ')
	text_nodes = text_to_textnodes(text)
	block_html_nodes = []
	for node in text_nodes:
		block_html_nodes.append(text_node_to_html_node(node))
	return block_html_nodes

def handle_paragraph_block(block):
	block_html_nodes = []
	text_nodes = text_to_textnodes(block)
	for node in text_nodes:
		block_html_nodes.append(text_node_to_html_node(node))
	return block_html_nodes

def get_block_text(block, splitter):
	if splitter == '```':
		return block.strip(splitter)
	return block.lstrip(splitter)

def block_type_to_html_tag(block, blocktype):
	match blocktype:
		case 'quote':
			return 'blockquote'
		case 'unordered_list':
			return 'ul'
		case 'ordered_list':
			return 'ol'
		case 'code':
			return 'pre'
		case 'heading':
			split = block.split()
			count = split[0].count('#')
			return f'h{count}'
		case 'paragraph':
			return 'p'
		case _:
			return ValueError('Error: Invalid block')

