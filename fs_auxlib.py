"""
fs_auxlib.py : file system auxiliary library
"""

import os

def clear_directory(folder):
    """
    Deletes all files and folders in 'folder'
    """
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)    

def clear_directory_files(folder):
    """
    Deletes all files in 'folder' (excludes folders)
    """
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def delete_file(file_path):
    """
    Deletes the file with path 'file_path' if it exists
    """
    if os.path.exists(file_path):
        os.unlink(file_path)