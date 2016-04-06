import os
import re


def remove_spaces(text: str):
    text = " ".join(text.split())
    return text


def is_valid_string(text: str):
    result = text and not text.isspace()
    return result


# TODO refactor code
# TODO add exception
def filename_from_url(url: str) -> str:
    filename = re.search("([^/?#]*\.[^/?#]*?$)", url)
    filename = filename.groups()[0]
    return filename


def decode_text(text):
    try:
        result = bytes(text, "latin1").decode("utf-8")
    except (UnicodeDecodeError, UnicodeEncodeError):
        # logging.warning("Unicode Warning: Can't handle decode.")
        pass
    return result


def clear_folder(directory: str):
    files = os.listdir(directory)
    for file in files:
        os.remove(directory + file)