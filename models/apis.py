import pymysql
from config.settings import DATABASES
from aiohttp import web
import decimal,json,datetime

async def api_users(request):
    # pass
    conn=pymysql.connect(**DATABASES)
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from users')
    users=cursor.fetchall()
    cursor.close()
    conn.close()
    print(type(users))
    data={'users':json.loads((json.dumps(users, cls=JSONEncoder)))}
    return web.json_response(data)



class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        return json.JSONEncoder.default(self, obj)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        return super().default(o) #初始化父类的实例调用上面相关的属性和方法。    
