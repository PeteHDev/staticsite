import re
from enum import Enum

class BlockType(Enum):
    P = "paragraph"
    H = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    newMarkdown = re.sub(r"\n[^\S\r\n]*", "\n", markdown)
    blocks = newMarkdown.split("\n\n")
    blocks = [item.strip() for item in blocks]
    blocks = [item for item in blocks if item]
    return blocks

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.H
    
    lines = block.split("\n")
    if len(lines) > 1 and lines[0].replace(" ", "") == "```" and lines[-1].startswith("```"):
        return BlockType.CODE
    
    quote = True
    unordered_list = True
    ordered_list = True
    i = 0
    while (quote or unordered_list or ordered_list) and i < len(lines):
        if quote and not lines[i].startswith(">"):
            quote = False
        
        if unordered_list and not lines[i].startswith("- "):
            unordered_list = False

        if ordered_list and not lines[i].startswith(f"{i+1}. "):
            ordered_list = False
        
        i += 1

    if quote:
        return BlockType.QUOTE
    elif unordered_list:
        return BlockType.U_LIST
    elif ordered_list:
        return BlockType.O_LIST
    else:
        return BlockType.P
