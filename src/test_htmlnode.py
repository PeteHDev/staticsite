import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

class TestHMTLNode(unittest.TestCase):
    def test_props_to_html_a(self):
        node = HTMLNode("a", "boot.dev", None, {"href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev"')

    def test_props_to_html_link(self):
        node = HTMLNode("link", None, None, {"rel": "stylesheet", "href": "styles.css"})
        self.assertEqual(node.props_to_html(), ' rel="stylesheet" href="styles.css"')

    def test_props_to_html_p(self):
        node1 = HTMLNode("p", "Some paragraph 1", None, None)
        node2 = HTMLNode("p", "Some paragraph 2", None, {})
        self.assertEqual(node1.props_to_html(), "")
        self.assertEqual(node2.props_to_html(), "")

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            ["a", "img", "br", "div"],
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: ['a', 'img', 'br', 'div'], {'class': 'primary'})",
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Boot.dev", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Boot.dev</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Some text", None)
        self.assertEqual(node.to_html(), "Some text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None, None)
        with self.assertRaises(ValueError):
            node.to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_wtih_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_chilndren_and_grandchildren(self):
        h1 = LeafNode("h1", "Title Header")
        link1 = LeafNode("a", "Link one", {"href": "https:/one.com"})
        link2 = LeafNode("a", "Link two", {"href": "https:/two.com"})
        link3 = LeafNode("a", "Link three", {"href": "https:/three.com"})
        div1 = ParentNode("div", [link1, link2, link3], {"class": "class_1"})
        p1 = LeafNode("p", "Paragraph one")
        p2 = LeafNode("p", "Paragraph two")
        p3 = LeafNode("p", "Paragraph three")
        div2 = ParentNode("div", [p1, p2, p3], {"class": "class_2"})
        body = ParentNode("body", [h1, div1, div2])
        html = ParentNode("html", [body])

        self.assertEqual(html.to_html(),
            '<html><body><h1>Title Header</h1><div class="class_1"><a href="https:/one.com">Link one</a><a href="https:/two.com">Link two</a><a href="https:/three.com">Link three</a></div><div class="class_2"><p>Paragraph one</p><p>Paragraph two</p><p>Paragraph three</p></div></body></html>')
        
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_bold(self):
        node = TextNode("This is a BOLD text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a BOLD text node")

    def test_text_italic(self):
        node = TextNode("This is a ITALIC text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a ITALIC text node")

    def test_text_code(self):
        node = TextNode("This is a CODE text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a CODE text node")

    def test_text_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_text_image(self):
        node = TextNode("Picture of Boot", TextType.IMAGE, "https://boot.dev/picture_of_boot.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://boot.dev/picture_of_boot.jpg", "alt": "Picture of Boot"})

    def test_text_exception(self):
        node = TextNode("Boot.dev", "LINK", "https://boot.dev")
        with self.assertRaises(TypeError):
            html_node = text_node_to_html_node(node)