# This is the main file for executing the program.
from textnode import (
    TextNode,
    text_type_text,
    text_type_link,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnode
)

import re

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    # expected = [
    #     TextNode("This is ", text_type_text),
    #     TextNode("text", text_type_bold),
    #     TextNode(" with an ", text_type_text),
    #     TextNode("italic", text_type_italic),
    #     TextNode(" word and a ", text_type_text),
    #     TextNode("code block", text_type_code),
    #     TextNode(" and an ", text_type_text),
    #     TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    #     TextNode(" and a ", text_type_text),
    #     TextNode("link", text_type_link, "https://boot.dev"),
    # ]
    expected = [
        TextNode("This is **text** with an *italic* word and a `code block` and an ", text_type_text),
        TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        TextNode(" and a ", text_type_text),
        TextNode("link", text_type_link, "https://boot.dev")
    ]

    print(f"{split_nodes_link(split_nodes_image([TextNode(text, text_type_text)]))} \n \n{expected} \n \n{text_to_textnode(text) == expected}")


main()