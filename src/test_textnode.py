import unittest

from textnode import TextNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test to make sure __eq__ is working correctly.
        node = TextNode("This is a text node", "text_type_bold")
        node2 = TextNode("This is a text node", "text_type_bold")
        self.assertEqual(node, node2)

        url_none = TextNode("This is a text node with None as url", "text_type_italic", None)
        url_none2 = TextNode("This is a text node with None as url", "text_type_italic")
        self.assertEqual(url_none, url_none2)

        leaf_node = LeafNode("b", "This is a text node")
        self.assertEqual(node.text_node_to_html_node(), leaf_node)

        image_text_node = TextNode("this is alt text", "text_type_image", "./public/test.jpg")
        image_leaf_node = LeafNode("img", "", {"src": "./public/test.jpg", "alt": "this is alt text"})
        self.assertEqual(image_text_node.text_node_to_html_node(), image_leaf_node)


if __name__ == "__main__":
    unittest.main()