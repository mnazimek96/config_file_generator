import os


def create_dirs():
    if not os.path.exists("output"):
        os.makedirs("output")

    if not os.path.exists("output/log"):
        os.makedirs("output/log")

    if not os.path.exists("output/backup"):
        os.makedirs("output/backup")

    if not os.path.exists("output/config"):
        os.makedirs("output/config")
