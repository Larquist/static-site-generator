class HTMLNode:
    # tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    # value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    # children - A list of HTMLNode objects representing the children of this node
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag.
    def __init__(self, tag = None, value = None, children = None, props = None):
        # Exceptions for values passed in
        if tag is not None and not isinstance(tag, str):
            raise Exception("Tag must be a string")
        if value is not None and not isinstance(value, str):
            raise Exception("Value must be a string")
        if children is not None and not isinstance(children, list):
            raise Exception("Children must be a list")
        if props is not None and not isinstance(props, dict):
            raise Exception("Props must be a dictionary")
        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # Child classes will override this method
    def to_html(self):
        raise NotImplementedError()
    
    # Returns a string representation of the HTML attributes
    # {"href": "https://www.google.com", "target": "_blank"} -> "href="https://www.google.com" target="_blank""
    def props_to_html(self):
        result = ""

        if self.props == None:
            return result

        # loop through dictionary & add to result
        for prop in self.props:
            result = result + f' {prop}="{self.props[prop]}"'
        
        return result
    

    def __repr__(self):
        return f"HTMLNode(self, {self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, target):
        return (self.tag == target.tag and 
                self.value == target.value and 
                self.children == target.children and 
                self.props == target.props)