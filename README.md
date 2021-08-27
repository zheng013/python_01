## aiohttp pymysql python 的mvc框架

```(lua)
——application --代表应用信息，包括路由的映射等
——config   项目一下配置信息，目录，数据库信息等
——template  映射的模板
——main.py  启动文件
       
```

## 使用UiKitcss框架
[uikitcss框架](https://getuikit.com/download)

## 后端API包括有
* 获取日志：GET /api/blogs

* 创建日志：POST /api/blogs

* 修改日志：POST /api/blogs/:blog_id

* 删除日志：POST /api/blogs/:blog_id/delete

* 获取评论：GET /api/comments

* 创建评论：POST /api/blogs/:blog_id/comments

* 删除评论：POST /api/comments/:comment_id/delete

* 创建新用户：POST /api/users

* 获取用户：GET /api/users

管理页面包括：

* 评论列表页：GET /manage/comments

* 日志列表页：GET /manage/blogs
  
* 创建日志页：GET /manage/blogs/create
  
* 修改日志页：GET /manage/blogs/

* 用户列表页：GET /manage/users

用户浏览页面包括：

* 注册页：GET /register

* 登录页：GET /signin

* 注销页：GET /signout

* 首页：GET /

* 日志详情页：GET /blog/:blog_id