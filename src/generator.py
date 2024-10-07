import os
import shutil
from block_markdown import markdown_to_html_node

def extract_title(markdown):
	split_lines = markdown.split('\n')
	for line in split_lines:
		if line.startswith('# '):
			return line.lstrip('#').strip()
	raise Exception("No title found")

def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")

	with open(from_path, 'r') as md_file:
		md_text = md_file.read()

	with open(template_path, 'r') as temp_file:
		template_text = temp_file.read()

	md_html_string = markdown_to_html_node(md_text).to_html()
	page_title = extract_title(md_text)

	template_text = template_text.replace("{{ Title }}", 
		page_title).replace("{{ Content }}", 
		md_html_string
	)

	if not os.path.exists(os.path.dirname(dest_path)):
		os.makedirs(os.path.dirname(dest_path))

	with open(dest_path, 'x') as new_html:
		new_html.write(template_text)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	folder_entries = os.listdir(dir_path_content)

	for entry in folder_entries:
		src_path = os.path.join(dir_path_content, entry)
		if os.path.isfile(src_path):
			if entry.endswith('.md'):
				filename = entry.rstrip('.md')
				dest_path = os.path.join(dest_dir_path, f'{filename}.html')
				generate_page(src_path, template_path, dest_path)
		elif os.path.isdir(src_path):
			dest_path = os.path.join(dest_dir_path, entry)
			#print(f'Dir Found: {dest_path}')
			generate_pages_recursive(src_path, template_path, dest_path)


def copy_static_to_public(src, dest):
	if not os.path.exists(src):
		raise ValueError(f"{src} path doesn't exist")

	print(f"Creating {dest} directory...")
	os.mkdir(dest)

	def copier(src, dest):
		paths = [f for f in os.listdir(src) if not f.startswith('.')]
		for path in paths:
			src_path = os.path.join(src, path)
			dest_path = os.path.join(dest, path)

			if not os.path.isfile(src_path):
				if not os.path.exists(dest_path):
					print(f"Creating {dest_path} directory...")
					os.mkdir(dest_path)
				copier(src_path, dest_path)
			else:
				print(f'Copying {src_path} to {dest_path}...')
				shutil.copy(src_path, dest_path)

	return copier(src, dest)