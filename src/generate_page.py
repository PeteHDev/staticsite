from blocks import markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node, block_to_html_node

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