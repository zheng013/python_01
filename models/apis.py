import pymysql,base64,aiohttp_session,time
from config.settings import DATABASES
from aiohttp import web
import decimal,json,datetime
from cryptography import fernet
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage


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

    
async def api_register(request):
    # pass
    post_data=await request.content.read()
    user_info=json.loads(post_data)
    conn=pymysql.connect(**DATABASES)
    name=user_info.get("name")
    passwd=user_info.get("passwd")
    email=user_info.get("email")
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from users where name=%s',(name))
    user=cursor.fetchall()
    if user:
        cursor.close()
        conn.close()
        return web.Response(text='当前用户已存在')
    else:
        cursor.execute('INSERT INTO users(name,email,password,image) VALUES(%s,%s,%s,%s)',(name,email,passwd,'sdsd'))
        conn.commit()
        cursor.close()
        conn.close()
        data={'users':json.loads((json.dumps(user, cls=JSONEncoder)))}
        res = web.Response()
        res.content_type='application/json'
        res.set_cookie('COOKIE_NAME_USERID', str.encode(passwd), max_age=86400, httponly=True)
        res.body=json.dumps(user_info)
        return res
async def  sign_in(request):
    session = await get_session(request)
    cookieid=request.cookies.get('AIOHTTP_SESSION')
    last_visit = session[cookieid] if 'last_visit' in session else None
    session[cookieid] = '大王'  # 将用户信息保存在session中，等再次登录后进行匹配获取正确的用户登录
    text = 'Last visited: {}'.format(last_visit)
    response=web.Response()
    aiohttp_session.save_session(request,response,session)
    # sessid= request.cookies.get('AIOHTTP_SESSION')
    # sessionStoragess=aiohttp_session.AbstractStorage(sessid)
    # print(sessionStoragess.load_cookie(request))
     # 将用户信息保存在session中，等再次登录后进行匹配获取正确的用户登录
    return web.json_response('ok')
async def  sign_in2(request):
    session = await get_session(request)
    cookieid=request.cookies.get('AIOHTTP_SESSION')
    last_visit = session[cookieid]
    session['last_visit'] = 2   # 将用户信息保存在session中，等再次登录后进行匹配获取正确的用户登录
    text = 'Last visited: {}'.format(session['last_visit'])
    # sessid= request.cookies.get('AIOHTTP_SESSION')
    # sessionStoragess=aiohttp_session.AbstractStorage(sessid)
    # print(sessionStoragess.load_cookie(request))
     # 将用户信息保存在session中，等再次登录后进行匹配获取正确的用户登录
    return web.json_response(text)

async def create_blog(request):
  post_data=await request.content.read()
  blog_data=json.loads(post_data)
  name=blog_data.get('name')
  summary=blog_data.get('summary')
  content=blog_data.get('content')
  conn =pymysql.connect(**DATABASES)
  cursor=conn.cursor(pymysql.cursors.DictCursor)
  cursor.execute('insert into blogs(user_id,user_name,user_image,name,summary,content,created_at) values(%s,%s,%s,%s,%s,%s,%s)',('test31','pable31','blank:about',name,summary,content,time.time()))
  conn.commit()
  cursor.execute('select *from blogs where name=%s',name)
  blog=cursor.fetchone()
  cursor.close()  #利用with进行替代 自动close
  conn.close()
  blog=json.loads((json.dumps(blog, cls=JSONEncoder)))
  return web.json_response(blog)

'''
对于当前的用户进行绑定到request的操作，对于管理页面进行权限控制。


@asyncio.coroutine
def auth_factory(app, handler):
    @asyncio.coroutine
    def auth(request):
        logging.info('check user: %s %s' % (request.method, request.path))
        request.__user__ = None
        cookie_str = request.cookies.get(COOKIE_NAME)
        if cookie_str:
            user = yield from cookie2user(cookie_str)
            if user:
                logging.info('set current user: %s' % user.email)
                request.__user__ = user
        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin):
            return web.HTTPFound('/signin')
        return (yield from handler(request))
    return auth
'''
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        return json.JSONEncoder.default(self, obj)

 
