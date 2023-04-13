from flask import Blueprint, render_template, request, current_app
from .models import Cookie
from app.orders.models import Order

blueprint = Blueprint('cookies', __name__)


@blueprint.route('/cookies/<slug>')
def cookie(slug):
  cookie = Cookie.query.filter_by(slug=slug).first_or_404()
  return render_template('cookies/show.html', cookie=cookie)

@blueprint.route('/cookies')
def cookies():
  page = request.args.get('page', 1, type=int)
  cookies_pagination = Cookie.query.paginate(page=page, per_page=current_app.config['COOKIES_PER_PAGE'])
  return render_template('cookies/index.html', cookies_pagination=cookies_pagination)


@blueprint.route('/view-orders')
def preview():
  orders=Order.query.all()
  return render_template('preview.html',orders=orders)

@blueprint.route('/run-seed')
def run_seed():
  if not Cookie.query.filter_by(slug='chocolate-chip').first():
    import app.scripts.seed
    return 'Database seed completed!'
  else:
    return 'Nothing to run.'

