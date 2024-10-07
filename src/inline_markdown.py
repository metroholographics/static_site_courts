import re

from textnode import (
	TextNode,
	t_t_text,
	t_t_bold, 	
	t_t_italic, 
	t_t_code, 
	t_t_link, 
	t_t_image,
)

def text_to_textnodes(text):
	nodes_list = [TextNode(text, t_t_text)]
	inline_formats = [('**', t_t_bold), ('*', t_t_italic), ('`', t_t_code)]
	for formats in inline_formats:
		nodes_list = split_nodes_delimiter(nodes_list, formats[0], formats[1])
	nodes_list = split_nodes_image(split_nodes_link(nodes_list))
	return nodes_list

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
		current_new_nodes = []
		if node.text_type == t_t_text:
			if node.text.count(delimiter) % 2 != 0:
				raise ValueError(f"Invalid number of delimiters: {node.text}")

			split_node = node.text.split(delimiter)

			for i in range(len(split_node)):
				if split_node[i] == '':
					continue
				if i % 2 == 0:
					current_new_nodes.append(TextNode(split_node[i], t_t_text))
				else:
					current_new_nodes.append(TextNode(split_node[i], text_type))
		else:
			new_nodes.append(node)
		new_nodes.extend(current_new_nodes)
	return new_nodes


def extract_markdown_images(text):
	return re.findall(r'!\[(.*?)\]\((.*?)\)', text)

def extract_markdown_links(text):
	return re.findall(r'(?<!!)\[(.*?)\]\((.*?)\)', text)

def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		current_list = []
		if node.text_type == t_t_text:
			link_list = extract_markdown_links(node.text)
			text_copy = node.text
			for link in link_list:
				link_anchor = link[0]
				link_url = link[1]
				text_copy = text_copy.split(f"[{link_anchor}]({link_url})", 1)
				if len(text_copy) != 2:
					raise ValueError("Invalid, link section not closed")
				if text_copy[0] != '':
					current_list.append(TextNode(text_copy[0], t_t_text))
				current_list.append(TextNode(link_anchor, t_t_link, link_url))
				text_copy = text_copy[1]
			if text_copy != '':
				current_list.append(TextNode(text_copy, t_t_text))
		else:
			new_nodes.append(node)
		new_nodes.extend(current_list)

	return new_nodes
		
def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
		current_list = []
		if node.text_type == t_t_text:
			link_list = extract_markdown_images(node.text)
			text_copy = node.text
			for link in link_list:
				link_alt_text = link[0]
				link_url = link[1]
				text_copy = text_copy.split(f"![{link_alt_text}]({link_url})", 1)
				if len(text_copy) != 2:
					raise ValueError("Invalid, image section not closed")
				if text_copy[0] != '':
					current_list.append(TextNode(text_copy[0], t_t_text))
				current_list.append(TextNode(link_alt_text, t_t_image, link_url))
				text_copy = text_copy[1]
			if text_copy != '':
				current_list.append(TextNode(text_copy, t_t_text))
		else:
			new_nodes.append(node)
		new_nodes.extend(current_list)

	return new_nodes





