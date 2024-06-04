import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test to make sure __eq__ is working correctly.
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        url_none = TextNode("This is a text node with None as url", "italic", None)
        url_none2 = TextNode("This is a text node with None as url", "italic")
        self.assertEqual(url_none, url_none2)

        leaf_node = LeafNode("b", "This is a text node")
        self.assertEqual(text_node_to_html_node(node), leaf_node)

        image_text_node = TextNode("this is alt text", "image", "./public/test.jpg")
        image_leaf_node = LeafNode("img", "", {"src": "./public/test.jpg", "alt": "this is alt text"})
        self.assertEqual(text_node_to_html_node(image_text_node), image_leaf_node)


if __name__ == "__main__":
    unittest.main()