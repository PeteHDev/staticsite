import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_simple(self):
        md = "# Simple Title"
        expected = "Simple Title"
        actual = extract_title(md)
        self.assertEqual(expected, actual)

    def test_extract_title_multiline(self):
        md = """
# A
Multiline
Heading
"""
        expected = "A Multiline Heading"
        actual = extract_title(md)
        self.assertEqual(expected, actual)

        md = """
           # A
Multiline
Heading
With
**Bold**
_Italic_
And
`Code`
Inline
Formatting
Removed
"""
        expected = "A Multiline Heading With Bold Italic And Code Inline Formatting Removed"
        actual = extract_title(md)
        self.assertEqual(expected, actual)
        
    def test_extract_title_missing(self):
        md = """
## A
Multiline
Heading
With
**Bold**
_Italic_
And
`Code`
Inline
Formatting
"""
        with self.assertRaises(Exception) as cm:  
            extract_title(md)
