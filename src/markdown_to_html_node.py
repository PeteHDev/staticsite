from blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        blockType = block_to_block_type(block)
    return blocks

def block_to_html_node(block, blockType):
    text = block_to_text(block, blockType)
    if blockType == BlockType.P:
        return ParentNode("p", None, None, None)
    elif blockType == BlockType.H:
        rank = len(block.split(" ", 1)[0])
        return ParentNode(f"h{rank}", block.lstrip("#"*rank + " "), None, None)
    elif blockType == BlockType.CODE:
        return ParentNode("code", block.strip("```"), None, None)
    elif blockType == BlockType.QUOTE:
        return ParentNode("blockquote", block, None, None)
    elif blockType == BlockType.U_LIST:
        return ParentNode("ul", block, None, None)
    elif blockType == BlockType.O_LIST:
        return ParentNode("ol", block, None, None)
    else:
        return ParentNode()
    
def block_to_text(block, blockType):
    if blockType == BlockType.H:
        return block.split(" ", 1)[1]
    elif blockType == BlockType.QUOTE or \
    blockType == BlockType.U_LIST or \
    blockType == BlockType.O_LIST:
        lines = block.split("\n")
        return "\n".join([cleanup_list_item(line) for line in lines])
    elif blockType == BlockType.CODE:
        return block.lstrip("```").rstrip("```")
    else:
        return block
    
def cleanup_list_item(item):
    split = item.split(" ", 1)
    if len(split) == 2:
        return split[1]
    return ""
def text_to_children(text):
    pass