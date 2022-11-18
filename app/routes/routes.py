import os

from flask import render_template, request, flash, redirect, url_for, send_file, jsonify, make_response
from sqlalchemy import and_, or_, update
from pathlib import Path
from IPython.display import Image
import json

from gtts import gTTS

# from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

# from werkzeug import secure_filename
from datetime import date

from app.utils.const import (
    TEMPLATE_DIR,
    STATIC_DIR,
    APP_NAME,
    UPLOAD_DIR,
    OUTPUT_DIR,
    CONFIG,
)
from app.utils.utils import empty_dir, check_extension, pdf_to_text

from app.app import app, db


@app.context_processor
def global_jinja_variables():
    return {"app_title": APP_NAME}


@app.route("/", methods=["GET", "POST"])
def home():
    # # # FILE UPLOAD
    if request.method == "POST":
        empty_dir(OUTPUT_DIR)

        f = request.files["file"]
        if f:
            if check_extension(f.filename):
                try:
                    filename = secure_filename(f.filename)
                    f.save(f"{UPLOAD_DIR}/{filename}")
                    # do something with file

                    return redirect(url_for("listen", filename=filename))
                except IOError as e:
                    app.logger.exception(e)
                    flash("Can't save and process file!", "error")
                flash("Do not know what happened!", "error")
            else:
                flash("The file does not a pdf!", "error")
        else:
            flash("Error while importing the file!", "error")

    return render_template("pages/index.html", title="Index")


@app.route("/listen/<filename>", methods=["GET"])
def listen(filename):
    if filename is None:
        flash("No filename provided", "error")
        return redirect(url_for("home"))

    if not os.path.isfile(UPLOAD_DIR / filename):
        flash("No file associated to the filename provided", "error")
        return redirect(url_for("home"))

    return render_template(
        "pages/view.html",
        file=pdf_to_text(filename.split('.')[0]),
        title="Listen your pdf",
    )

# @app.route("/post", methods=["POST"])
# def post():
#     res = request.get_json()
#     # do something
#     return jsonify({"response": True})
