import os
from blocks import markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node, block_to_html_node
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    md = None
    with open(from_path) as f:
        md = f.read()

    template = None
    with open(template_path) as f:
        template = f.read()

    print(f"Generating page from {from_path} to {dest_path}...")

    title = extract_title(md)
    node = markdown_to_html_node(md)
    html = node.to_html()
    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)
    
    if os.path.exists(dest_path):
        with open(dest_path, "w") as f:
            f.write(page)
        return
    
    dir_name = os.path.dirname(dest_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    with open(dest_path, "x") as f:
        f.write(page)
    

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