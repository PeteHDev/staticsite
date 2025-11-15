from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://garbage.org")
    print(node)

main()