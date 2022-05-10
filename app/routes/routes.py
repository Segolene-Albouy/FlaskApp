from flask import render_template, request, flash, redirect, url_for, send_file
from sqlalchemy import and_, or_, update

# from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

# from werkzeug import secure_filename
from datetime import date

from app.utils.const import TEMPLATE_DIR, STATIC_DIR, APP_NAME, CONFIG

from app.app import app, db


@app.context_processor
def global_jinja_variables():
    return {"app_title": APP_NAME}


@app.route("/", methods=["GET", "POST"])
def home():
    # person = Person.query.all()
    return render_template("pages/index.html", title="Index")


# @app.route("/post", methods=["POST"])
# def post():
#     res = request.get_json()
#     these = Thesis.query.get(res["id"])
#     Response.add_response(these, res["answer"])
#     return jsonify({"response": True})
