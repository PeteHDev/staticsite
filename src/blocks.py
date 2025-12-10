import re

def markdown_to_blocks(markdown):
    newMarkdown = re.sub(r"\n[^\S\r\n]*", "\n", markdown)
    blocks = newMarkdown.split("\n\n")
    blocks = [item.strip() for item in blocks]
    blocks = [item for item in blocks if item]
    return blocks
