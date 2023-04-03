from flask import Flask, redirect, url_for, render_template, send_file
from . import cookies
from flask_sqlalchemy import SQLAlchemy
from random import randint

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('app.config')

app.register_blueprint(cookies.routes.blueprint)

@app.route('/')
def index():
  name = 'Sam'
  fake_number = 342
  return render_template('index.html', name=name, visitor_number=fake_number)

@app.route('/about')
def about():
  return 'I like cookies'

#example of a redirect
@app.route('/about-me')
def about_me():
  return redirect(url_for('about'))

#Download route
#as atachment parameter triggers download
@app.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment=True)


    