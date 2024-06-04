from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props =None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag must be provided")

        if self.children == None:
            raise ValueError("Child values must be provided in a parent node")

        content = ""

        for child in self.children:
            content = content + child.to_html()

        # <par><child>text</child><child>more text</child></par>
        return f"<{self.tag + self.props_to_html()}>{content}</{self.tag}>"