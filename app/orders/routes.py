from flask import Blueprint, render_template, request
from app.cookies.models import Cookie
from .services.create_order import create_order


blueprint = Blueprint('orders', __name__)

@blueprint.get('/checkout')
def get_checkout():
  cookies = Cookie.query.all()
  return render_template('orders/new.html', cookies=cookies)

@blueprint.post('/checkout')
def post_checkout():
  cookies = Cookie.query.all()

  create_order(request.form, cookies)

  return render_template('orders/new.html', cookies=cookies)