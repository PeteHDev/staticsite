import unittest

from textnode import TextNode, TextType, split_into_code_nodes

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text mode", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_missing(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_into_code_nodes(self):
        node_no_code = TextNode("There is no code here", TextType.TEXT)
        self.assertEqual(split_into_code_nodes(node_no_code), ["There is no code here"])

        node_one_code_block = TextNode("Only one `code` block", TextType.TEXT)
        self.assertEqual(split_into_code_nodes(node_one_code_block), ["Only one ", 
                                                                      TextNode("code", TextType.CODE), 
                                                                      " block"])
        
        node_all_code = TextNode("`ALL CODE`", TextType.TEXT)
        self.assertEqual(split_into_code_nodes(node_all_code), [TextNode("ALL CODE", TextType.CODE)])

        node_two_code_blocks = TextNode("`First code block` and `Second code block`", TextType.TEXT)
        self.assertEqual(split_into_code_nodes(node_two_code_blocks), [TextNode("First code block", TextType.CODE),
                                                                       " and ",
                                                                       TextNode("Second code block", TextType.CODE)])
if __name__ == "__main__":
    unittest.main()