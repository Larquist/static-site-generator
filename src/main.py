# This is the main file for executing the program.
from textnode import (
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

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    
    
    print(text_to_textnode(text))


main()