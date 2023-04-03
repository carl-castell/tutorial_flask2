from flask import Flask
from . import cookies, simple_pages
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('app.config')

#Blueprints
app.register_blueprint(cookies.routes.blueprint)
app.register_blueprint(simple_pages.routes.blueprint)

