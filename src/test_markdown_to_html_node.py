import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdwonToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_lists(self):
        md1 = """
    1. oi1
    2. oi2
    3. oi3
    """

        node1 = markdown_to_html_node(md1)
        html1 = node1.to_html()
        self.assertEqual(
            html1,
            "<div><ol><li>oi1</li><li>oi2</li><li>oi3</li></ol></div>"
        )

        md2 = """
    - ui1
    - ui2
    - ui3
    """
        
        node2 = markdown_to_html_node(md2)
        html2 = node2.to_html()
        self.assertEqual(
            html2,
            "<div><ul><li>ui1</li><li>ui2</li><li>ui3</li></ul></div>"
        )

        md3 = """
    >Some **bold** quote
    >Some _italic_ quote
    >Some inline `code` quote 
    """

        node3 = markdown_to_html_node(md3)
        html3 = node3.to_html()
        self.assertEqual(
            html3,
            "<div><blockquote>Some <b>bold</b> quote Some <i>italic</i> quote Some inline <code>code</code> quote</blockquote></div>"
        )

    def test_headings(self):
        md = """
    # H1

    ## H2

    ### H3

    #### H4

    ##### H5

    ###### H6

    ####### Paragraph
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>H1</h1><h2>H2</h2><h3>H3</h3><h4>H4</h4><h5>H5</h5><h6>H6</h6><p>####### Paragraph</p></div>"
        )

    def test_mixed_blocks(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```

    1. oi1
    2. oi2
    3. oi3

    - ui1
    - ui2
    - ui3

    >Some **bold** quote
    >Some _italic_ quote
    >Some inline `code` quote 

    # H1

    ## H2

    ### H3

    #### H4

    ##### H5

    ###### H6

    ####### Paragraph
    """
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre><ol><li>oi1</li><li>oi2</li><li>oi3</li></ol><ul><li>ui1</li><li>ui2</li><li>ui3</li></ul><blockquote>Some <b>bold</b> quote Some <i>italic</i> quote Some inline <code>code</code> quote</blockquote><h1>H1</h1><h2>H2</h2><h3>H3</h3><h4>H4</h4><h5>H5</h5><h6>H6</h6><p>####### Paragraph</p></div>"
        )
