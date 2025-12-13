from blocks import markdown_to_blocks, block_to_block_type, BlockType
from textnode import text_to_textnodes, TextNode, TextType
from htmlnode import text_node_to_html_node, ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        node = block_to_html_node(block)
        if not node:
            continue
        children.append(node)
    return ParentNode("div", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.P:
        return paragraph_to_html_node(block)
    elif block_type == BlockType.H:
        return heading_to_html_node(block)
    elif block_type == BlockType.CODE:
        return code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    elif block_type == BlockType.O_LIST:
        return ordered_list_to_html_node(block)
    elif block_type == BlockType.U_LIST:
        return unordered_list_to_html_node(block)
    else:
        return None

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return children

def paragraph_to_html_node(block):
    if block_to_block_type(block) != BlockType.P:
        raise ValueError("invalid paragraph block")
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    if block_to_block_type(block) != BlockType.H:
        raise ValueError("invalid heading block")
    marker_and_text = block.split(" ", 1)
    tag = f"h{len(marker_and_text[0])}"
    if len(marker_and_text) == 1:
        return ParentNode(tag, text_to_children(""))
    
    return ParentNode(tag, text_to_children(marker_and_text[1]))

def cleanup_list_item(item):
    split = item.split(" ", 1)
    if len(split) == 1:
        return ""
    return split[1]

def quote_to_html_node(block):
    if block_to_block_type(block) != BlockType.QUOTE:
        raise ValueError("invalid quote block")
    lines = block.split("\n")
    items = [line[1:] for line in lines]
    text = " ".join(items)
    return ParentNode("blockquote", text_to_children(text))

def list_children(block):
    lines = block.split("\n")
    items = [cleanup_list_item(line) for line in lines]
    return [ParentNode("li", text_to_children(item)) for item in items]

def ordered_list_to_html_node(block):
    if block_to_block_type(block) != BlockType.O_LIST:
        raise ValueError("invalid ordered list block")
    return ParentNode("ol", list_children(block))

def unordered_list_to_html_node(block):
    if block_to_block_type(block) != BlockType.U_LIST:
        raise ValueError("invalid unordered list block")
    return ParentNode("ul", list_children(block))

def code_to_html_node(block):
    if block_to_block_type(block) != BlockType.CODE:
        raise ValueError("invalid code block")
    lines = block.split("\n")
    lines[-1] = ""
    text = "\n".join(lines[1:])
    text_node = TextNode(text, TextType.CODE)
    children = [text_node_to_html_node(text_node)]
    return ParentNode("pre", children)
