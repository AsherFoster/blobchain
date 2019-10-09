import process


def main():
    """It's pretty simple at the moment. Just grab that, mutate it, and shove it back"""
    # These paths are relative to the root dir
    old_path = './previous.png'
    new_path = './output.png'

    process.process(old_path, new_path)


main()
