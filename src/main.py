import os
import shutil
from textnode import TextNode, TextType
from markdown_to_html_node import markdown_to_html_node
from util import copy_files_from_to
from generate_page import extract_title, generate_page_recursive

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    
    try:
        copy_files_from_to("static", "public")
        generate_page_recursive("content", "template.html", "public")
    except Exception as err:
        print(f"error: {err}")
        exit(1)

main()