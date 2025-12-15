import re
import os
import shutil

def extract_markdown_images(text):
    markdown_image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    markdown_images = re.findall(markdown_image_pattern, text)

    return markdown_images

def extract_markdown_links(text):
    markdown_link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    markdown_links = re.findall(markdown_link_pattern, text)

    return markdown_links

def copy_files_from_to(src_path, dst_path):
    if not os.path.exists(src_path):
        raise ValueError(f"error: src path <{src_path}> does not exist")
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    
    for item in os.listdir(src_path):
        full_path = os.path.join(src_path, item)
        if os.path.isfile(full_path):
            print(f"Copying file {full_path}...")
            shutil.copy(full_path, dst_path)
        else:
            print(f"Copying subdirectory {full_path}...")
            dst_subdir = os.path.join(dst_path, item)
            copy_files_from_to(full_path, dst_subdir)

def cleanup_folder(path):
    if os.path.exists(path):
        if not os.path.isdir(path):
            raise ValueError(f"error: destination <{path}> is not a directory")
        shutil.rmtree(path)
    else:
        print(f"Creating {os.path.join(os.getcwd(), path)} directory")

    os.mkdir(path)

