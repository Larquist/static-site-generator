from leafnode import LeafNode
    
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    # text = text content of the node
    # text_type = type of text the node contains, eg. bold, italics
    # url = URL of link or image, default is None if nothing is passed
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # Compare TextNode objects
    def __eq__(self, target):
        return (self.text == target.text and 
            self.text_type == target.text_type and 
            self.url == target.url)

    # String representation of the TextNode object
    def __repr__(self):
        return f"TextNode(self, {self.text}, {self.text_type}, {self.url})"

# Convert textnode to htmlnode
def text_node_to_html_node(node):
    if node.text_type == text_type_text:
        return LeafNode(None, node.text)
    if node.text_type == text_type_bold:
        return LeafNode("b", node.text)
    if node.text_type == text_type_italic:
        return LeafNode("i", node.text)
    if node.text_type == text_type_code:
        return LeafNode("code", node.text)
    if node.text_type == text_type_link:
        return LeafNode("a", node.text, {"href": node.url})
    if node.text_type == text_type_image:
        return LeafNode("img", "", {"src": node.url, "alt": node.text})
    raise Exception("text_type of TextNode not valid")
        
