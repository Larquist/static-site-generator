import re

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
        return f"TextNode(self, '{self.text}', '{self.text_type}', {self.url})"

# Convert textnode to htmlnode(LeafNode)
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
        
# old_nodes = list of nodes
# delimiter = the symbol to look for
# text_type = the textnode type to set the segmented text to
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    # Step through old_nodes list
    for node in old_nodes:
        split_text = node.text.split(delimiter)
        # If length of list is 1, no delimiter was found
        if len(split_text) == 1:
            new_nodes.append(node)
        # If len of list is even, it means only one symbol was found in the list
        elif len(split_text) % 2 == 0:
            raise Exception(f"Closing symbol not found: {delimiter}")
        else:
            for i in range(0, len(split_text)):
                if split_text[i] != '':
                    # If index is even or the first index, it will be a regular text node
                    if i % 2 == 0 or i == 0:
                        new_nodes.append(TextNode(split_text[i], text_type_text))
                    # If index is odd, it is the desired text to seperate
                    else:
                        new_nodes.append(TextNode(split_text[i], text_type))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        # If node is not a text text_type, then just append it to the list 
        # - No action required
        if node.text_type != "text":
            new_nodes.append(node)
            break
        text = node.text

        # Extract images from the text eg. 
        # [
        # ('test','testlink.com'),
        # ('test2','testlink2.com')
        # ]
        images = extract_markdown_images(text)

        # If length is 0, means there are no images present, just return 
        # the current node as is
        if len(images) == 0:
            new_nodes.append(node)
        else:
            for i in range(0, len(images)):
                # Split at current image, will leave behind text before and
                # text after the image
                split = text.split(f"![{images[i][0]}]({images[i][1]})")
                # Target last index of images list
                if i == len(images) - 1:
                    if split[1] == "":
                        # If the text after the image split contains
                        # nothing, it means that we can just append a
                        # text_type_text then the text_type_image
                        new_nodes.append(TextNode(split[0], text_type_text))
                        new_nodes.append(TextNode(images[i][0], text_type_image, images[i][1]))
                        break
                    else:
                        # Else we add text0, image, text1
                        new_nodes.append(TextNode(split[0], text_type_text))
                        new_nodes.append(TextNode(images[i][0],
                        text_type_image,
                        images[i][1]))
                        new_nodes.append(TextNode(split[1], text_type_text))
                        break
                

                if split[0] == "":
                    # append only image because no text came before
                    new_nodes.append(TextNode(images[i][0],
                    text_type_image, 
                    images[i][1]))
                else:
                    # Append text before image and image
                    new_nodes.append(TextNode(split[0], text_type_text))
                    new_nodes.append(TextNode(images[i][0],
                    text_type_image,
                    images[i][1]))

                # Make text the text after the image so it can be further 
                # processed in the loop
                text = split[1]

    return new_nodes
                

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            break

        text = node.text

        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(node)
        else:
            for i in range(0, len(links)):
                split = text.split(f"[{links[i][0]}]({links[i][1]})")
                if i == len(links) - 1:
                    if split[1] == "":
                        new_nodes.append(TextNode(split[0], text_type_text))
                        new_nodes.append(TextNode(links[i][0], text_type_link, links[i][1]))
                        break
                    else:
                        new_nodes.append(TextNode(split[0], text_type_text))
                        new_nodes.append(TextNode(links[i][0],
                        text_type_link,
                        links[i][1]))
                        new_nodes.append(TextNode(split[1], text_type_text))
                        break
                

                if split[0] == "":
                    new_nodes.append(TextNode(links[i][0],
                    text_type_link, 
                    links[i][1]))
                else:
                    new_nodes.append(TextNode(split[0], text_type_text))
                    new_nodes.append(TextNode(links[i][0],
                    text_type_link,
                    links[i][1]))

                text = split[1]

    return new_nodes

# Takes raw text and returns a tuple with alt text and the url of the image
# !\[(.*?)\]\((.*?)\) - Regex expression for capturing
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def text_to_textnode(text):
    split_images = split_nodes_image([TextNode(text, text_type_text)])
    split_links = split_nodes_link(split_images)
    split_code = split_nodes_delimiter(split_links, "`", text_type_code)
    split_bold = split_nodes_delimiter(split_code, "**", text_type_bold)
    split_italic = split_nodes_delimiter(split_bold, "*", text_type_italic)
    return split_italic