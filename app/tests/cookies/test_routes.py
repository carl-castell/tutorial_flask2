from app.cookies.models import Cookie

def test_cookies_renders_cookies(client):
  # Page loads and renders cookies
  new_cookie = Cookie(slug='chocolate-chip', name='Chocolate Chip', price=1.50)
  new_cookie.save()

  response = client.get('/cookies')
  
  assert b'Chocolate Chip' in response.data
  
  
def test_cookies_renders_cookies_example(client):
  # Page loads and renders one example of a cookie and its price
  new_cookie = Cookie(slug='test', name='Example Test', price=3.23)
  new_cookie.save()

  response = client.get('/cookies/test')
  
  assert b'3.23' in response.data