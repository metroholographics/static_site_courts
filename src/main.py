from generator import *

static_path = './static'
public_path = './public'
content_path = './content'

def main():
	if os.path.exists(public_path):
		shutil.rmtree(public_path)

	copy_static_to_public(static_path, public_path)
	generate_pages_recursive(content_path, './template.html', public_path)


if __name__ == "__main__":
	main()