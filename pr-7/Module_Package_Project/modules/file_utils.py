import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def _get_path(filename):
    return os.path.join(DATA_DIR, filename)


def create_file(filename):
    path = _get_path(filename)
    with open(path, "w") as f:
        pass
    print("File created successfully!")


def write_to_file(filename, data):
    path = _get_path(filename)
    with open(path, "w") as f:
        f.write(data)
    print("Data written successfully!")


def read_from_file(filename):
    path = _get_path(filename)
    try:
        with open(path, "r") as f:
            content = f.read()
        print(f"File Content:\n{content}")
    except FileNotFoundError:
        print("File not found!")


def append_to_file(filename, data):
    path = _get_path(filename)
    with open(path, "a") as f:
        f.write(data + "\n")
    print("Data appended successfully!")
