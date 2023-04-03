from flask import Flask, redirect, url_for, render_template, send_file
from flask_sqlalchemy import SQLAlchemy
from random import randint

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('config')

cookies_data = {
  'chocolate-chip' : {'name': 'Chocolate Chip', 'price': '$1.50'},
  'oatmeal-raisin' : {'name': 'Oatmeal Raisin', 'price': '$1.00'},
  'sugar' : {'name': 'Sugar', 'price': '$0.75'},
  'peanut-butter' : {'name': 'Peanut Butter', 'price': '$0.50'},
  'oatmeal' : {'name': 'Oatmeal', 'price': '$0.25'},
  'salted-caramel' : {'name': 'Salted Caramel', 'price': '$1.00'},
}

@app.route('/')
def index():
  name = 'Sam'
  fake_number = 342
  return render_template('index.html', name=name, visitor_number=fake_number)


# Funktionirt mit dictinary. Variante drunter arbeitet mit einer liste
#@app.route('/cookies/<slug>')
#def cookie(slug):
#  if slug in cookies_data:
#    return '<h1>' + cookies_data[slug]['name'] + '</h1>' + '<p>' + cookies_data[slug]['price'] + '</p>'
#  else:
#    return 'Sorry we could not find that cookie.' 

@app.route('/cookies')
def cookies():
  cookies = cookies_data
  return render_template('cookies.html', cookies=cookies)

@app.route('/cookies/<slug>')
def cookie(slug):
  return '<h1>' + cookies_data[slug]['name'] + '</h1>' + '<p>' + cookies_data[slug]['price'] + '</p>'

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

if __name__ == '__main__':
    app.run()
    