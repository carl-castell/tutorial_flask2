def serialize_orders(orders):
  orders_list = []
  
  for order in orders:
      orders_list.append({
          'id': order.id,
          'date': order.date.strftime('%Y-%m-%d %H:%M:%S'),
          'address': {
            'name': order.address.name,
            'street': order.address.street,
            'city': order.address.city,
            'state': order.address.state,
            'zip': order.address.zip,
            'country': order.address.country
          },
          'cookie_orders': serialize_cookie_orders(order.cookie_orders)
      })
  
  return orders_list


def serialize_cookie_orders(cookie_orders):
  cookie_orders_list = []

  for cookie_order in cookie_orders:
    cookie_orders_list.append({
      'cookie_id': cookie_order.cookie_id,
      'number_of_cookies': cookie_order.number_of_cookies,
      'cookie_name': cookie_order.cookie.name
    })

  return cookie_orders_list