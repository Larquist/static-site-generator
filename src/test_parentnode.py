import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        # TEST #1 - Just Leaf nodes
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)
        # print("Parent node test #1:\n", 
        # "Expected:", expected, "\n"
        # "Actual:", node.to_html())

        # TEST #2 - w/ Parent node inside
        node2 = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                node,
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected2 = "<div><b>Bold text</b><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</div>"
        self.assertEqual(node2.to_html(), expected2)
        # print("Parent node test #2:\n", 
        # "Expected:", expected2, "\n"
        # "Actual:", node2.to_html())
        
        

if __name__ == "__main__":
    unittest.main()