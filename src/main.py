from textnode import TextNode, TextType
from markdown_to_html_node import markdown_to_html_node
from util import copy_files_from_to

def main():
    copy_files_from_to("static", "public")

main()