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
    
    cleanup_folder(dst_path)
    
    for item in os.listdir(src_path):
        if os.path.isfile(item):
            print(f"Copying {item}...")
            shutil.copy(item, dst_path)
        else:
            src_subdir = os.path.join(src_path, item)
            print(f"Copying {src_subdir}...")
            dst_subdir = os.path.join(dst_path, item)
            copy_files_from_to(src_subdir, dst_subdir)

    

def cleanup_folder(path):
    if os.path.exists(path):
        if not os.path.isdir(path):
            raise ValueError(f"error: destination <{path}> is not a directory")
        shutil.rmtree(path)
    else:
        print(f"Destination {path} folder does not exist...")
        print("Creating...")

    os.mkdir(path)
    print("Cleanup destination: " + os.path.join(os.getcwd(), path))


