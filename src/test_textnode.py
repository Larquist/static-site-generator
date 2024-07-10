import unittest

from textnode import(
    TextNode,
    text_type_text,
    text_type_link,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_node_to_html_node
)
from inline import(
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnode
)
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test to make sure __eq__ is working correctly.
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        # Should equal
        url_none = TextNode("This is a text node with None as url", "italic", None)
        url_none2 = TextNode("This is a text node with None as url", "italic")
        self.assertEqual(url_none, url_none2)


    def test_text_node_to_html_node(self):
        # Should equal
        node = TextNode("This is a text node", "bold")
        leaf_node = LeafNode("b", "This is a text node")
        self.assertEqual(text_node_to_html_node(node), leaf_node)

        image_text_node = TextNode("this is alt text", "image", "./public/test.jpg")
        image_leaf_node = LeafNode("img", "", {"src": "./public/test.jpg", "alt": "this is alt text"})
        self.assertEqual(text_node_to_html_node(image_text_node), image_leaf_node)

    
    def test_split_nodes_delimiter(self):
        # Bold block test variables
        node = TextNode("This is text with a *bold* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text)
        ]

        # Code block test variables
        node2 = TextNode("This is a `code block`", text_type_code)
        new_nodes2 = split_nodes_delimiter([node2], "`", text_type_code)
        expected2 = [
            TextNode("This is a ", text_type_text),
            TextNode("code block", text_type_code)
        ]

        # 2 nodes expected test variable
        new_nodes3 = split_nodes_delimiter([node, node2], '*', text_type_bold)
        new_nodes4 = split_nodes_delimiter(new_nodes3, "`", text_type_code)
        expected3 = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
            TextNode("This is a ", text_type_text),
            TextNode("code block", text_type_code)
        ]

        self.assertEqual(new_nodes, expected)
        self.assertEqual(new_nodes2, expected2)
        self.assertEqual(new_nodes4, expected3)

        # Error test
        node3 = TextNode("This is text with a *bold word", text_type_bold)
        expected4 = Exception("Closing symbol not found: *")
        with self.assertRaises(Exception):
            split_nodes_delimiter([node3], "*", text_type_bold)


    def test_extract_markdown_images(self):
        text_one_image = "This is a ![test image](https://github.com/larquist/test_image.jpg) right back there."
        text_multiple_image = "This is a ![test image](https://github.com/larquist/test_image.jpg) right back there. Here is ![another](https://test.com/image.jpg)"
        text_broken_image = "This is a !test image](https://github.com/larquist/test_image.jpg) right back there."
        text_link = "This is a [test link](https://github.com/larquist/test_image.jpg) right back there."

        self.assertEqual(extract_markdown_images(text_one_image), [
            ('test image', 'https://github.com/larquist/test_image.jpg')
        ])
        self.assertEqual(extract_markdown_images(text_multiple_image), [
            ('test image', 'https://github.com/larquist/test_image.jpg'),
            ("another", "https://test.com/image.jpg")
        ])
        self.assertNotEqual(extract_markdown_images(text_broken_image), [
            [
            ('test image', 'https://github.com/larquist/test_image.jpg')
            ]   
        ])
        self.assertEqual(extract_markdown_images(text_link), [])


    def test_extract_markdown_links(self):
        text_one_link = "This is a [test link](https://github.com/larquist/test_link.jpg) right back there."
        text_multiple_link = "This is a [test link](https://github.com/larquist/test_link.jpg) right back there. Here is [another](https://test.com/link.jpg)"
        text_broken_link = "This is a [test link]https://github.com/larquist/test_link.jpg) right back there."

        self.assertEqual(extract_markdown_links(text_one_link), [
            ('test link', 'https://github.com/larquist/test_link.jpg')
        ])
        self.assertEqual(extract_markdown_links(text_multiple_link), [
            ('test link', 'https://github.com/larquist/test_link.jpg'),
            ("another", "https://test.com/link.jpg")
        ])
        self.assertNotEqual(extract_markdown_links(text_broken_link), [
            [
            ('test link', 'https://github.com/larquist/test_link.jpg')
            ]   
        ])


    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        broken_node = TextNode(
            "This is text with an !image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image]https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]
        
        self.assertEqual(split_nodes_image([node]), expected)
        self.assertEqual(split_nodes_image([broken_node]), [
            TextNode("This is text with an !image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image]https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text_type_text)
        ])


    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        broken_node = TextNode(
            "This is text with an !link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second link]https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]
        
        self.assertEqual(split_nodes_link([node]), expected)
        self.assertEqual(split_nodes_link([broken_node]), [
            TextNode("This is text with an !link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second link]https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text_type_text)
        ])


    def test_text_to_textnode(self):
            self.maxDiff = None
            text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
            expected = [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ]

            self.assertEqual(text_to_textnode(text), expected)


if __name__ == "__main__":
    unittest.main()