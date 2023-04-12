from flask import Blueprint, render_template, request
from app.cookies.models import Cookie
from app.orders.models import Order, Address

blueprint = Blueprint('orders', __name__)

@blueprint.get('/checkout')
def get_checkout():
  cookies = Cookie.query.all()
  return render_template('orders/new.html', cookies=cookies)

@blueprint.post('/checkout')
def post_checkout():
  # Create an order
  order = Order()
  order.save()
  
  # Create an Adress linked to an Order
  address = Address(
      name=request.form.get('name'),
      street=request.form.get('street'),
      city=request.form.get('city'),
      state=request.form.get('state'),
      zip=request.form.get('zip'),
      country=request.form.get('country'),
      order=order
  )
  address.save()

  cookies = Cookie.query.all()
  return render_template('orders/new.html', cookies=cookies)