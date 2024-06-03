import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        child_node = HTMLNode("a", "link", None, {"href": "https://test.com"})
        node = HTMLNode("h1", "test", [child_node], None)
        node2 = HTMLNode("h1", "test", [child_node], None)
        self.assertEqual(node, node2)

        self.assertNotEqual(child_node, node)

        props_to_html_expected = ' href="https://test.com"'
        self.assertEqual(child_node.props_to_html(), props_to_html_expected)

if __name__ == "__main__":
    unittest.main()