import re

def extract_markdown_images(text):
    markdown_image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    markdown_images = re.findall(markdown_image_pattern, text)

    return markdown_images

def extract_markdown_links(text):
    markdown_link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    markdown_links = re.findall(markdown_link_pattern, text)

    return markdown_links