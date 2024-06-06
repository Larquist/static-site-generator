# This is the main file for executing the program.
from textnode import (
    TextNode,
    text_type_text,
    text_type_link,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    split_nodes_delimiter
)

def main():
    node = TextNode("This is text with a *bold word", text_type_bold)
    new_nodes = split_nodes_delimiter([node], "*", text_type_bold)

    print(new_nodes)


main()