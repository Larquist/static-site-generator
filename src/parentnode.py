from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props =None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag must be provided")

        if self.children == None:
            raise ValueError("Child values must be provided in a parent node")

    