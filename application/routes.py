from .views import hello,users
import aiohttp_jinja2,jinja2
from config.settings import STATIC_DIR, TEMPLATE_DIR


def setup_template_routes(app):
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


def  setup_routes(app):
    app.router.add_get('/hello',hello)
    app.router.add_get('/users',users)