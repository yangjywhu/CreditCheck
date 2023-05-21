import os

def create_dir(dir_name):    
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def list_format_file(dir_name, fmt, full_path = False):
    dir_pfx = dir_name if full_path else ""
    filtered_files = []

    for file_name in os.listdir(dir_name):
        if file_name[-len(fmt):] != fmt:
            continue
        new_name = os.path.join(dir_pfx, file_name)
        filtered_files.append(new_name)
    
    return filtered_files