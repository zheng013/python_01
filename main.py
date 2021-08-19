from aiohttp import web
from application.routes import setup_routes,  setup_template_routes,setup_static_routes,setup_api_routes


def init():
    app = web.Application()
    setup_routes(app)
    setup_template_routes(app)
    setup_static_routes(app)
    setup_api_routes(app)
    return app

app=init()

web.run_app(app,host='localhost',port=9000)