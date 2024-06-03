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

    
