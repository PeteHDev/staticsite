from textnode import TextNode, TextType
from markdown_to_html_node import markdown_to_html_node

def main():
    md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    ```
    This is a block of code
    ```

    """
    print(markdown_to_html_node(md))

main()