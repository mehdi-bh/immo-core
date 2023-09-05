from flask import Flask
from src.routes import user_routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_routes.user_routes, url_prefix='/api')
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
