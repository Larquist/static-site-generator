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
    one = extract_markdown_images("This is a ![test image](https://github.com/larquist/test_image.jpg) right back there.")
    two = [
            TextNode("This is a ", text_type_text),
            TextNode("test image", text_type_image, "https://github.com/larquist/test_image.jpg"),
            TextNode(" right back there.", text_type_text)
        ]
    print(one, two, one == two)


main()