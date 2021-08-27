import asyncio,base64,time
from aiohttp import web
from application.routes import setup_routes,setup_template_routes,setup_static_routes,setup_api_routes
from cryptography import fernet
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage

def init():
    app = web.Application()
    setup_routes(app)
    setup_template_routes(app)
    setup_static_routes(app)
    setup_api_routes(app)
    return app

async def handler(request):
    session = await get_session(request)
    last_visit = session['last_visit'] if 'last_visit' in session else None
    session['last_visit'] = time.time()   # 将用户信息保存在session中，等再次登录后进行匹配获取正确的用户登录
    text = 'Last visited: {}'.format(last_visit)
    return web.Response(text=text)

async def make_app():
    app=init()
    # secret_key must be 32 url-safe base64-encoded bytes
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    app.add_routes([web.get('/', handler)])
    return app

web.run_app(make_app(),host='localhost',port=9000)






