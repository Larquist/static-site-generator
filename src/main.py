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
    extract_markdown_links
)

import re

def main():
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text))


main()