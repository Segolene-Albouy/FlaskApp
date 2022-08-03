from app.app import config_app, app

if __name__ == "__main__":
    app = config_app()
    app.run(debug=True)
