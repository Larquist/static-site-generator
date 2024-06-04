class TextNode:
    from leafnode import LeafNode
    
    valid_types = [
            "text_type_text",
            "text_type_bold",
            "text_type_italic",
            "text_type_code",
            "text_type_link",
            "text_type_image"
        ]

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
    def text_node_to_html_node(self):
        if self.text_type not in self.valid_types:
            raise Exception("text_type of TextNode not valid")

        if self.text_type == "text_type_text":
            return self.LeafNode(None, self.text)
        if self.text_type == "text_type_bold":
            return self.LeafNode("b", self.text)
        if self.text_type == "text_type_italic":
            return self.LeafNode("i", self.text)
        if self.text_type == "text_type_code":
            return self.LeafNode("code", self.text)
        if self.text_type == "text_type_link":
            return self.LeafNode("a", self.text, {"href": self.url})
        if self.text_type == "text_type_image":
            return self.LeafNode("img", "", {"src": self.url, "alt": self.text})
        
