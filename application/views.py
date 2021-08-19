import pymysql
from config.settings import DATABASES
import aiohttp_jinja2
from aiohttp import web


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


async def hello(request):
    return web.Response(text='Hello,World!')