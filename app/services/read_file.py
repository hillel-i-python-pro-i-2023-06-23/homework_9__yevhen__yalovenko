import pathlib

from app.config import FILES_INPUT_DIR
from app.loggers.loggers import get_custom_logger


def read_file(path: pathlib.Path = None):
    if path is None:
        path = FILES_INPUT_DIR.joinpath("hello_world.txt")

    file_to_read = read_txt(txt_file_path=path)
    return file_to_read


def read_txt(txt_file_path: pathlib.Path) -> str:
    logger = get_custom_logger(__name__)

    with open(txt_file_path, "r") as txt_file:
        text = txt_file.read()

    logger.info(f"txt file with random text is read: {txt_file_path.as_uri()}")
    return text
