import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks_basic(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_excessive_indentation(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_excessive_newlines(self):
        md = """
    This is **bolded** paragraph

    



    

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    






    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockType(unittest.TestCase):
    def test_block_type_heading(self):
        block1 = "# 1st level Heading"
        block2 = "## 2nd level Heading"
        block3 = "### 3rd level Heading"
        block4 = "#### 4th level Heading"
        block5 = "##### 5th level Heading"
        block6 = "###### 6th level Heading"
        block7 = "####### not a Heading"
        block8 = "asd ### not a Heading"
        block9 = "# H"
        block10 = ""

        self.assertEqual(block_to_block_type(block1), BlockType.H)
        self.assertEqual(block_to_block_type(block2), BlockType.H)
        self.assertEqual(block_to_block_type(block3), BlockType.H)
        self.assertEqual(block_to_block_type(block4), BlockType.H)
        self.assertEqual(block_to_block_type(block5), BlockType.H)
        self.assertEqual(block_to_block_type(block6), BlockType.H)
        self.assertEqual(block_to_block_type(block7), BlockType.P)
        self.assertEqual(block_to_block_type(block8), BlockType.P)
        self.assertEqual(block_to_block_type(block9), BlockType.H)
        self.assertEqual(block_to_block_type(block10), BlockType.P)
        
    def test_block_type_code(self):
        code = "```print('Hello, World!')\nprint('Hello, World! Again!')\nprint('Hello, World! Again...')```"
        not_code = "``print('Hello, World!')``"

        self.assertEqual(block_to_block_type(code), BlockType.CODE)
        self.assertEqual(block_to_block_type(not_code), BlockType.P)

    def test_block_type_quote(self):
        quote = """>Some
>Kind
>of
>Quote"""

        not_quote = """>Some
Kind
>of
Not Quote"""

        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(not_quote), BlockType.P)

    def test_block_type_unordered_list(self):
        unordered_list = """- Some
- Kind
- of
- Unordered
- List"""

        not_unordered_list = """- Some
Kind
of
- Unordered
- List"""

        self.assertEqual(block_to_block_type(unordered_list), BlockType.U_LIST)
        self.assertEqual(block_to_block_type(not_unordered_list), BlockType.P)

    def test_block_type_unordered_list(self):
        ordered_list = """1. Some
2. Kind
3. of
4. Unordered
5. List"""
        invalid_ordered_list1 = """2. Some
3. Kind
4. of
5. Unordered
6. List"""
        invalid_ordered_list2 = """1. Some
2. Kind
4. of
3. Unordered
6. List"""
        not_ordered_list = """1. Some
Kind
of
2. Unordered
3. List"""

        self.assertEqual(block_to_block_type(ordered_list), BlockType.O_LIST)
        self.assertEqual(block_to_block_type(invalid_ordered_list1), BlockType.P)
        self.assertEqual(block_to_block_type(invalid_ordered_list2), BlockType.P)
        self.assertEqual(block_to_block_type(not_ordered_list), BlockType.P)
