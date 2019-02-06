from app import app
from flask import render_template

# 使用模板1 - 模板
# 使用模板2 - 模板中控制语句
# -----------------
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
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'calvino'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'calvino 1'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'calvino 2'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'calvino 3'},
            'body': 'I am the third one!'
        }
    ]
    return render_template("index.html",
                        #    title='Home',
                           user=user,
                           posts=posts)
