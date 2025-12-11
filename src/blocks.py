import re
from enum import Enum

class BlockType(Enum):
    P = 1
    H = 2
    CODE = 3
    QUOTE = 4
    U_LIST = 5
    O_LIST = 6

def markdown_to_blocks(markdown):
    newMarkdown = re.sub(r"\n[^\S\r\n]*", "\n", markdown)
    blocks = newMarkdown.split("\n\n")
    blocks = [item.strip() for item in blocks]
    blocks = [item for item in blocks if item]
    return blocks

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.H
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")
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
