import unittest

from util import extract_markdown_images, extract_markdown_links

class TestLinksExtraction(unittest.TestCase):
    def test_extract_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_imageS(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                              ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
    
    def test_extract_markdown_linkS(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),
                              ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
        
    def test_extract_markdown_links_and_images(self):
        images = extract_markdown_images(
            '''This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)
            This is text with a link [to boot dev](https://www.boot.dev)
            This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and 
            ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
            This is text with a link [to boot dev](https://www.boot.dev) and 
            [to youtube](https://www.youtube.com/@bootdotdev)'''
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),
                              ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                              ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], images)
        
        links = extract_markdown_links(
            '''This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)
            This is text with a link [to boot dev](https://www.boot.dev)
            This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and 
            ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
            This is text with a link [to boot dev](https://www.boot.dev) and 
            [to youtube](https://www.youtube.com/@bootdotdev)'''
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),
                              ("to boot dev", "https://www.boot.dev"),
                              ("to youtube", "https://www.youtube.com/@bootdotdev")], links)