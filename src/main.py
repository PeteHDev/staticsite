import os
import shutil
import sys
from textnode import TextNode, TextType
from markdown_to_html_node import markdown_to_html_node
from util import copy_files_from_to
from generate_page import extract_title, generate_page_recursive

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists("public"):
        shutil.rmtree("public")
    
    try:
        copy_files_from_to("static", "docs")
        generate_page_recursive("content", "template.html", "docs", basepath)
    except Exception as err:
        print(f"error: {err}")
        exit(1)

main()