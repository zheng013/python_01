import pymysql
from config.settings import DATABASES
import aiohttp_jinja2
from aiohttp import web
import time

@aiohttp_jinja2.template('user.html')
async def users(request):
    # pass
    conn=pymysql.connect(**DATABASES)
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from users')
    users=cursor.fetchall()
    cursor.close()
    conn.close()
    return {'users':users}
@aiohttp_jinja2.template('blogs.html')
async def blogs(request):
    # pass
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        {'id':'1', 'name':'Test Blog','summary':summary, 'created_at':time.time()-120},
        {'id':'2', 'name':'Something New', 'summary':summary, 'created_at':time.time()-3600},
        {'id':'3', 'name':'Learn Swift', 'summary':summary, 'created_at':time.time()-720}
    ]
    return{'blogs':blogs}

async def hello(request):
    return web.Response(text='Hello,World!')

@aiohttp_jinja2.template('register.html')
async def register(request):
    pass
