from flask import render_template, request, flash, redirect, url_for, send_file
from sqlalchemy import and_, or_, update
from pathlib import Path
from IPython.display import Image
import json

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
from app.utils.utils import empty_dir, check_extension

from app.app import app, db


@app.context_processor
def global_jinja_variables():
    return {"app_title": APP_NAME}


@app.route("/", methods=["GET", "POST"])
def home():
    # # # IMAGE UPLOAD
    if request.method == "POST":
        empty_dir(OUTPUT_DIR)

        f = request.files["file"]  # request.files.get('image_name')
        if f:
            if check_extension(f.filename):
                try:
                    filename = secure_filename(f.filename)
                    idx = 0
                    filepath = Path(UPLOAD_DIR) / filename
                    f.save(filepath)
                    img = Image.open(filepath)

                    # do something with image

                    return redirect(url_for("prepare", id=idx))
                except IOError as e:
                    app.logger.exception(e)
                    flash("Can't save and process file!", "error")
                flash("Do not know what happened!", "error")
            else:
                flash("The file does not have the correct extension!", "error")
        else:
            flash("Error while importing the file!", "error")

    return render_template("pages/index.html", title="Index")
    # person = Person.query.all()


# @app.route("/post", methods=["POST"])
# def post():
#     res = request.get_json()
#     these = Thesis.query.get(res["id"])
#     Response.add_response(these, res["answer"])
#     return jsonify({"response": True})
