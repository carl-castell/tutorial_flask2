from app.app import create_app
from app.cookies.models import Cookie
from app.extensions.database import db

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()
  
cookies_data = {
  'chocolate-chip' : {'name': 'Chocolate Chip', 'price': 1.50},
  'oatmeal-raisin' : {'name': 'Oatmeal Raisin', 'price': 1.00},
  'sugar' : {'name': 'Sugar', 'price': 0.75},
  'peanut-butter' : {'name': 'Peanut Butter', 'price': 0.50},
  'oatmeal' : {'name': 'Oatmeal', 'price': 0.25},
  'salted-caramel' : {'name': 'Salted Caramel', 'price': 1.00},
  'vanilla' : {'name': 'Vanilla', 'price': 2.60},
  'rasperry' : {'name': 'Raspberry', 'price': 5.00},
  'mint' : {'name': 'Mint', 'price': 4.30},
  'lemon-apple' : {'name': 'Lemon Apple', 'price': 2.90},
  'grannys-special' : {'name': 'Grannys Special', 'price': 9.99},
}
  
for slug, cookie in cookies_data.items():
  new_cookie = Cookie(slug=slug, name=cookie['name'], price=cookie['price'])
  db.session.add(new_cookie)

db.session.commit()
