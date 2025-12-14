import re
import os

def extract_markdown_images(text):
    markdown_image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    markdown_images = re.findall(markdown_image_pattern, text)

    return markdown_images

def extract_markdown_links(text):
    markdown_link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    markdown_links = re.findall(markdown_link_pattern, text)

    return markdown_links

def copy_files_from_to(source_path, destination_path):
    if not os.path.exists(source_path):
        raise ValueError(f"error: source path <{source_path}> does not exist")
    if os.path.exists(destination_path):
        if not os.path.isdir(destination_path):
            raise ValueError(f"error: cannot copy to destination <{destination_path}>; it is not a directory")
    else:
        print("Destination folder does not exist...")
        print("Creating...")
        print(os.path.join(os.getcwd(), destination_path))
        os.mkdir(destination_path)
    

    return