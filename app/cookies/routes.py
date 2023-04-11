from flask import Blueprint, render_template
from .models import Cookie

blueprint = Blueprint('cookies', __name__)


@blueprint.route('/cookies/<slug>')
def cookie(slug):
  cookie = Cookie.query.filter_by(slug=slug).first_or_404()
  return render_template('cookies/show.html', cookie=cookie)

@blueprint.route('/cookies')
def cookies():
  all_cookies = Cookie.query.all()
  return render_template('cookies/index.html', cookies=all_cookies)