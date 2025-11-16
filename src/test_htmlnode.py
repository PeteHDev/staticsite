import unittest

from htmlnode import HTMLNode, LeafNode

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