from textnode import TextNode, TextType
from markdown_to_html_node import markdown_to_html_node
from util import copy_files_from_to
from generate_page import extract_title

def main():
    #copy_files_from_to("static", "public")
    md = """
# Hello
This is **bold** title
With multiple _lines_
"""
    try:
        print(extract_title(md))
    except EOFError as e:
        print(f"error: {e}")
main()