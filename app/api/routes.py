from flask import Blueprint

blueprint = Blueprint('api', __name__)

@blueprint.get('/api/v1/orders')
def orders():
  return {
    "data" : "Hello World"
  }