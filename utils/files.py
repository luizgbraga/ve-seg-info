from typing import Any


def save_to(file_path: str, key: Any):
    with open(file_path, "w") as file:
        file.write(str(key))
