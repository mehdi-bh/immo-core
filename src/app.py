from flask import Flask
from routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    init_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
