import os


def get_files_recursively(path):
    # Recursively fetch all files from a path and return a file, filepath dictionary
    temp = dict()
    for root, directories, filenames in os.walk(path):
        for directory in directories:
            os.path.join(root, directory)
        for filename in filenames:
            temp[filename] = os.path.join(root, filename)
    return temp

get_files("E:\\Testing")
