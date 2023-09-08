from flask import Flask
from src.routes import user_routes
from src.routes import apartment_routes
from src.routes import search_routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_routes.user_routes, url_prefix='/api')
    app.register_blueprint(apartment_routes.apartment_routes, url_prefix='/api')
    app.register_blueprint(search_routes.search_routes, url_prefix='/api')
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
