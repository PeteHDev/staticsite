import unittest

from textnode import TextNode, TextType, split_text_node_into_sub_nodes, split_nodes_delimiter

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
        self.assertEqual(split_text_node_into_sub_nodes(node_no_code, "`", TextType.CODE), 
                         [TextNode("There is no code here", TextType.TEXT)])

        node_one_code_block = TextNode("Only one `code` block", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_one_code_block, "`", TextType.CODE), 
                         [TextNode("Only one ", TextType.TEXT), 
                          TextNode("code", TextType.CODE), 
                          TextNode(" block", TextType.TEXT)])
        
        node_all_code = TextNode("`ALL CODE`", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_all_code, "`", TextType.CODE), 
                         [TextNode("ALL CODE", TextType.CODE)])

        node_two_code_blocks = TextNode("`First code block` and `Second code block`", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_two_code_blocks, "`", TextType.CODE), 
                         [TextNode("First code block", TextType.CODE), 
                          TextNode(" and ", TextType.TEXT),
                          TextNode("Second code block", TextType.CODE)])
        
        node_invalid_markdown = TextNode("Some `cOdE", TextType.TEXT)
        with self.assertRaises(Exception):
            split_text_node_into_sub_nodes(node_invalid_markdown, "`", TextType.CODE)

    def test_split_into_bold_nodes(self):
        node_no_BOLD = TextNode("There is no BOLD here", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_no_BOLD, "**", TextType.BOLD), 
                         [TextNode("There is no BOLD here", TextType.TEXT)])

        node_one_BOLD_block = TextNode("Only one **BOLD** block", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_one_BOLD_block, "**", TextType.BOLD), 
                         [TextNode("Only one ", TextType.TEXT), 
                          TextNode("BOLD", TextType.BOLD), 
                          TextNode(" block", TextType.TEXT)])
        
        node_all_BOLD = TextNode("**ALL BOLD**", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_all_BOLD, "**", TextType.BOLD), 
                         [TextNode("ALL BOLD", TextType.BOLD)])

        node_two_BOLD_blocks = TextNode("**First BOLD block** and **Second BOLD block**", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_two_BOLD_blocks, "**", TextType.BOLD), 
                         [TextNode("First BOLD block", TextType.BOLD), 
                          TextNode(" and ", TextType.TEXT),
                          TextNode("Second BOLD block", TextType.BOLD)])
        
        node_invalid_markdown = TextNode("Some **BOLD", TextType.TEXT)
        with self.assertRaises(Exception):
            split_text_node_into_sub_nodes(node_invalid_markdown, "**", TextType.BOLD)

    def test_split_into_italic_nodes(self):
        node_no_ITALIC = TextNode("There is no ITALIC here", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_no_ITALIC, "_", TextType.ITALIC), 
                         [TextNode("There is no ITALIC here", TextType.TEXT)])

        node_one_ITALIC_block = TextNode("Only one _ITALIC_ block", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_one_ITALIC_block, "_", TextType.ITALIC), 
                         [TextNode("Only one ", TextType.TEXT), 
                          TextNode("ITALIC", TextType.ITALIC), 
                          TextNode(" block", TextType.TEXT)])
        
        node_all_ITALIC = TextNode("_ALL ITALIC_", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_all_ITALIC, "_", TextType.ITALIC), 
                         [TextNode("ALL ITALIC", TextType.ITALIC)])

        node_two_ITALIC_blocks = TextNode("_First ITALIC block_ and _Second ITALIC block_", TextType.TEXT)
        self.assertEqual(split_text_node_into_sub_nodes(node_two_ITALIC_blocks, "_", TextType.ITALIC), 
                         [TextNode("First ITALIC block", TextType.ITALIC), 
                          TextNode(" and ", TextType.TEXT),
                          TextNode("Second ITALIC block", TextType.ITALIC)])
        
        node_invalid_markdown = TextNode("Some _ITALIC", TextType.TEXT)
        with self.assertRaises(Exception):
            split_text_node_into_sub_nodes(node_invalid_markdown, "_", TextType.ITALIC)

    def test_split_node_delimiter(self):
        nodes = [TextNode("_ITALIC_ **BOLD** `CODE`", TextType.TEXT)]
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(nodes, [TextNode("ITALIC", TextType.ITALIC),
                                 TextNode(" ", TextType.TEXT), 
                                 TextNode("BOLD", TextType.BOLD),
                                 TextNode(" ", TextType.TEXT),
                                 TextNode("CODE", TextType.CODE)])
        
    def test_split_node_delimiter_invalid(self):
        nodes = [TextNode("This is **a text node **with invalid markdown** (odd number of delimiters)", TextType.TEXT)]
        with self.assertRaises(Exception):
            nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        nodes = [TextNode("This `is **a text` node **with invalid markdown (mixed)", TextType.TEXT)]
        with self.assertRaises(Exception):
            nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
            nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

        
if __name__ == "__main__":
    unittest.main()