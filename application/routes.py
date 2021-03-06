from .views import hello,users,blogs,register,blog_edit
from models.apis import api_users,api_register,sign_in,sign_in2,create_blog
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
    app.router.add_get('/blog_edit',blog_edit)
    app.router.add_get('/blog_edit/{id}',blog_edit)
    app.router.add_get('/register',register) 


def  setup_api_routes(app):
    app.router.add_get('/api/users',api_users) 
    app.router.add_post('/api/register',api_register) 
    app.router.add_get('/api/signIn',sign_in) 
    app.router.add_get('/api/signIn2',sign_in2) 
    app.router.add_post('/create/blog',create_blog) 