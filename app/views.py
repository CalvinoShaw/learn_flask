# 使用模板1 - 模板
# 使用模板2 - 模板中控制语句
# -----------------
# from app import app
# from flask import render_template

# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'nickname': 'Calvino'}  # fake user
#     return render_template("index.html",
#                            title='YourHome',
#                            user=user)


# 使用模板3 - 模板中的循环语句
# 使用模板4 - 模板继承
# -----------------
# from app import app
# from flask import render_template

# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'nickname': 'calvino'}  # fake user
#     posts = [  # fake array of posts
#         {
#             'author': {'nickname': 'calvino 1'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'nickname': 'calvino 2'},
#             'body': 'The Avengers movie was so cool!'
#         },
#         {
#             'author': {'nickname': 'calvino 3'},
#             'body': 'I am the third one!'
#         }
#     ]
#     return render_template("index.html",
#                         #    title='Home',
#                            user=user,
#                            posts=posts)


# web表单1 - 表单视图
# -----------------
# from .forms import LoginForm@app.route('/login', methods=['GET', 'POST'])
# from app import app
# from flask import render_template, flash, redirect
# from .forms import LoginForm

# # 为简洁起见，索引视图功能被抑制
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template('login.html',
#                            title='标题登录',
#                            form=form)


# web表单4 - 接收表单数据
# -----------------
# from app import app
# from flask import render_template, flash, redirect
# from .forms import LoginForm

# @app.route('/loginsuccessed')
# def loginsuccessed():
#     return "表单提交成功！"

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     # validate_on_submit() 方法做了所有表单处理工作
#     if form.validate_on_submit():
#         # flash 函数是一种快速的方式下呈现给用户的页面上显示一个消息
#         # flash 函数在生产服务器上也是十分有作用的，用来提供反馈给用户有关的行动
#         flash('---flash() 函数处理数据: 账号 OpenID = "' + form.openid.data + '", 是否记住账号 remember_me=' + str(form.remember_me.data))
#         # redirect() 函数告诉网页浏览器引导到一个不同的页面而不是请求的页面
#         # return redirect('/loginsuccessed')
#     return render_template('login.html',
#                            title='标题登录',
#                            form=form)

# web表单6 - 处理 OpenIDs
from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/loginsuccessed')
def loginsuccessed():
    return "表单提交成功！"

@app.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('---flash() 函数处理数据: 账号 OpenID = "' + form.openid.data + '", 是否记住账号 remember_me=' + str(form.remember_me.data))
        # return redirect('/loginsuccessed')
    # 我们从配置中获取 OPENID_PROVIDERS，接着把它作为 render_template 中一个参数传入模板中
    return render_template('login.html',
                           title='标题登录',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
