import os
import re
import shutil
from pathlib import Path
from io import StringIO

from gtts import gTTS
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from app.utils.const import VALID_EXTENSIONS, UPLOAD_DIR, OUTPUT_DIR


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


def cid_to_char(cidx):
    return chr(int(re.findall(r'\(cid\:(\d+)\)', cidx)[0]) + 29)


def process_cid(text):
    processed_text = ""
    for x in text.split('\n'):
        if x != '' and x != '(cid:3)':  # merely to compact the output
            abc = re.findall(r'\(cid\:\d+\)', x)
            if len(abc) > 0:
                for cid in abc:
                    x = x.replace(cid, cid_to_char(cid))
            processed_text += repr(x).strip("'") + "\n"
    return processed_text


def extract_text(filename):
    if not os.path.isfile(f"{UPLOAD_DIR}/{filename}.pdf"):
        return "Not existing pdf file"

    output_text = StringIO()
    with open(f"{UPLOAD_DIR}/{filename}.pdf", 'rb') as content:
        manager = PDFResourceManager()
        device = TextConverter(manager, output_text, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, device)
        for page in PDFPage.create_pages(PDFDocument(PDFParser(content))):
            interpreter.process_page(page)

    text = process_cid(output_text.getvalue())
    print(text)
    return text if text else "No text was extracted from the pdf"


def pdf_to_text(filename):
    if os.path.isfile(f"{OUTPUT_DIR}/{filename}.wav"):
        os.remove(f"{OUTPUT_DIR}/{filename}.wav")

    text = extract_text(filename)
    try:
        sound = gTTS(text=text, lang='en', slow=False)
        sound.save(f"{OUTPUT_DIR}/{filename}.wav")
    except AssertionError as e:
        sound = gTTS(text="Error during pdf to sound conversion", lang='en', slow=False)
        sound.save(f"{OUTPUT_DIR}/{filename}.wav")

    return f"{filename}.wav"
