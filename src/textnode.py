from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        new_nodes.extend(split_text_node_into_sub_nodes(old_node, delimiter, text_type))
    
    return new_nodes


def split_text_node_into_sub_nodes(text_node, delimiter, text_type):
    split = text_node.text.split(delimiter)
    L = len(split)
    if L == 1:
        return split
    if L % 2 == 0:
        raise Exception(f"invalid Markdown: <{delimiter}> delimiter has to be closed")
    
    for i in range(1, len(split), 2):
        split[i] = TextNode(split[i], text_type)

    return [node for node in split if (isinstance(node, str) and node != "") or not isinstance(node, str)]

