import re
import shutil
from pathlib import Path

from app.utils.const import VALID_EXTENSIONS


def empty_dir(path):
    output_path = Path(path)
    if output_path.exists():
        shutil.rmtree(output_path)
    return create_dir(path)


def check_path(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError("{} does not exist".format(path.absolute()))
    return path


def create_dir(path):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def text_int(text):
    return int(text) if text.isdigit() else text


def sort_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    """
    return [text_int(c) for c in re.split(r"(\d+)", text)]


def get_files_from_dir(dir_path, valid_extensions=None, recursive=False, sort=False):
    path = check_path(dir_path)
    if recursive:
        files = [f.absolute() for f in path.glob("**/*") if f.is_file()]
    else:
        files = [f.absolute() for f in path.glob("*") if f.is_file()]

    if valid_extensions is not None:
        valid_extensions = (
            [valid_extensions]
            if isinstance(valid_extensions, str)
            else valid_extensions
        )
        valid_extensions = [
            ".{}".format(ext) if not ext.startswith(".") else ext
            for ext in valid_extensions
        ]
        files = list(filter(lambda f: f.suffix in valid_extensions, files))

    for i in range(len(files)):
        files[i] = str(files[i])

    files = sorted(files, key=sort_keys) if sort else files

    for i in range(len(files)):
        files[i] = Path(files[i])

    return files


def check_extension(filename=""):
    """ Returns True if the file has a correct extension """
    return "." in filename and filename.rsplit(".", 1)[1] in VALID_EXTENSIONS
