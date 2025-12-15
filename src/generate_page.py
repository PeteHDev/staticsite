import os
from blocks import markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node, block_to_html_node
from pathlib import Path

def generate_page(from_path, template_path, dest_path, basepath):
    if not os.path.isfile(from_path):
        raise Exception(f"source {from_path} does not exist or is not a file")
    
    if os.path.exists(dest_path) and os.path.isfile(dest_path):
        raise Exception(f"destination {dest_path} is a file, not a directory")

    md = None
    with open(from_path) as f:
        md = f.read()

    template = None
    with open(template_path) as f:
        template = f.read()

    path = Path(from_path)
    dest_dir_name = os.path.dirname(dest_path)
    dest_file = os.path.join(dest_dir_name, path.stem + ".html")

    print(f"Generating page from {from_path} to {dest_file}...")

    title = extract_title(md)
    node = markdown_to_html_node(md)
    embedded_html = node.to_html()
    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", embedded_html)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')
    
    if os.path.exists(dest_file):
        with open(dest_file, "w") as f:
            f.write(page)
        return
    
    dir_name = os.path.dirname(dest_file)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    with open(dest_file, "x") as f:
        f.write(page)

def generate_page_recursive(from_path, template_path, dest_path, basepath):
    if not os.path.exists(from_path):
        raise Exception(f"path {from_path} does not exist")
    
    if os.path.isfile(from_path):
        generate_page(from_path, template_path, dest_path, basepath)
        return

    for item in os.listdir(from_path):
        sub_from_path = os.path.join(from_path, item)
        sub_dest_path = os.path.join(dest_path, item)
        generate_page_recursive(sub_from_path, template_path, sub_dest_path, basepath)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return clean_title(block.split(" ", 1)[1])

    raise Exception("missing title")

def clean_title(title):
    clean = title.replace("*", "")
    clean = clean.replace("_", "")
    clean = clean.replace("`", "")

    lines = clean.split("\n")

    return " ".join(lines)