from flask import Blueprint, jsonify, request
from .services.serialize_orders import serialize_orders
from ..orders.models import Order
from os import environ

blueprint = Blueprint('api', __name__)

@blueprint.get('/api/v1/orders')
def orders():
  if environ.get('API_KEY') == request.headers.get('X-API-KEY'):
    orders = Order.query.all()
    return jsonify(
      serialize_orders(orders)
    )
  else:
    return jsonify({'error': 'Invalid API key'}), 401