from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.utils.const import TEMPLATE_DIR, STATIC_DIR, APP_NAME, CONFIG
from app.models.model import Person #, db
from app.routes import routes

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)

db = SQLAlchemy()

# @app.context_processor
# def global_jinja_variables():
#     return {"app_title": APP_NAME}
#
#
# @app.route("/", methods=["GET", "POST"])
# def home():
#     # person = Person.query.all()
#     return render_template(
#         "pages/index.html",
#         nom="app",
#     )


# @app.route("/post", methods=["POST"])
# def post():
#     res = request.get_json()
#     these = Thesis.query.get(res["id"])
#     Response.add_response(these, res["answer"])
#     return jsonify({"response": True})


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
migrate = Migrate(app, db)


def config_app(config_name="dev"):
    """ Create the application """
    db.init_app(app)
    db.app = app
    db.create_all()
    app.config.from_object(CONFIG[config_name])
    return app


if __name__ == "__main__":
    # config_app()
    app.run(debug=True)
