import os


def create_dirs():
    if not os.path.exists("output"):
        os.makedirs("output")

    if not os.path.exists("backup"):
        os.makedirs("backup")

