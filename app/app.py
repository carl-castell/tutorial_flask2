from flask import Flask
from . import cookies, simple_pages
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  register_blueprints(app)

  return app

# Blueprints
def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)
  app.register_blueprint(simple_pages.routes.blueprint)