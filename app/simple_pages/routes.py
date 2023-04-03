from flask import Blueprint, render_template, redirect, url_for, send_file

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
  name = 'Sam'
  fake_number = 342
  return render_template('index.html', name=name, visitor_number=fake_number)

@blueprint.route('/about')
def about():
  return 'I like cookies'

#example of a redirect
@blueprint.route('/about-me')
def about_me():
  return redirect(url_for('about'))

#Download route
#as atachment parameter triggers download
@blueprint.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment=True)

