from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.utils.const import TEMPLATE_DIR, STATIC_DIR, APP_NAME, CONFIG

# from app.models.model import db, Person

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

db = SQLAlchemy()

# import must be made after app initialisation, this import allows routes to be loaded even if the variable is not used
from app.routes import routes

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database.db"
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
