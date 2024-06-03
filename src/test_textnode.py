import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test to make sure __eq__ is working correctly.
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        url_none = TextNode("This is a text node with None as url", "italic", None)
        url_none2 = TextNode("This is a text node with None as url", "italic")
        self.assertEqual(url_none, url_none2)

        # url_diff = TextNode("This is original", "bold", "https://github/larquist/1")
        # url_diff2 = TextNode("This is different", "bold", "https://github/larquist/1")
        # self.assertEqual(url_diff, url_diff2)
        


if __name__ == "__main__":
    unittest.main()