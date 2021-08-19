from .views import hello,users,blogs
from models.apis import api_users
import aiohttp_jinja2,jinja2
from config.settings import STATIC_DIR, TEMPLATE_DIR


def setup_template_routes(app):
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
def setup_static_routes(app):
    app.router.add_static('/static/', path=STATIC_DIR, name='static')

def  setup_routes(app):
    app.router.add_get('/hello',hello)
    app.router.add_get('/users',users) 
    app.router.add_get('/blogs',blogs) 


def  setup_api_routes(app):
    app.router.add_get('/api/users',api_users) 