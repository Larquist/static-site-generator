import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "link", {"href": "https://test.com", "target": "_blank"})
        expected_html = '<a href="https://test.com" target="_blank">link</a>'
        self.assertEqual(node.to_html(), expected_html)

        node2 = LeafNode("p", "this is a paragraph")
        expected_html2 = "<p>this is a paragraph</p>"
        self.assertEqual(node2.to_html(), expected_html2)
        

if __name__ == "__main__":
    unittest.main()