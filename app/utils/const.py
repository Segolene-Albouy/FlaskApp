import os
from pathlib import Path
from warnings import warn

SECRET_KEY = "SECRET KEY!"
ROOT_DIR = Path(
    os.path.dirname(os.path.abspath(__file__)).split("FlaskApp", 1)[0] + "FlaskApp"
)
APP_DIR = Path(__file__).parent.parent
TEMPLATE_DIR = APP_DIR / "templates/"
STATIC_DIR = APP_DIR / "static/"
UPLOAD_DIR = STATIC_DIR / "uploads/"
OUTPUT_DIR = STATIC_DIR / "outputs/"

APP_NAME = "FlaskApp"

VALID_EXTENSIONS = ["jpeg", "JPEG", "jpg", "JPG", "pdf", "tiff"]

db = (
    os.environ.get("DATABASE_URL")
    if os.environ.get("DATABASE_URL") is None
    else "sqlite:///database.db"
)


class _TEST:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = db
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class _PRODUCTION:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = db
    SQLALCHEMY_TRACK_MODIFICATIONS = False


if SECRET_KEY == "SECRET KEY!":
    warn("Key hasn't been changed, you should do it", Warning)


class _DEVELOPMENT:
    SECRET_KEY = SECRET_KEY


class _PRODUCTION:
    SECRET_KEY = "IamS3CR37"


CONFIG = {"dev": _DEVELOPMENT, "prod": _PRODUCTION}
