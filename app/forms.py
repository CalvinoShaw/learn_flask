# 导入 Form 类
# 原代码：from flask.ext.wtf import Form，报错
# 方案一：首先看看是不是确保安装了flask.ext，命令 pip install flask-script
# 方案二：把 .ext. 换成 _ 就好了
from flask_wtf import Form
# 导入两个我们需要的字段类，TextField 和 BooleanField
from wtforms import StringField, BooleanField
# 导入 DataRequired 验证器，用于简单地检查相应域提交的数据是否是空
from wtforms.validators import DataRequired

class LoginForm(Form):
    # StringField 是一个文本输入框
    # 可以增加 validators 作为验证器
    openid = StringField('openid',
                        validators=[DataRequired()]
                        )
    # BooleanField 是一个单选框
    # default 字段表示默认是否勾选，false 为默认不勾选
    # 同样可以增加 validators 作为验证器
    remember_me = BooleanField('remember_me', 
                                default=False, 
                                validators=[DataRequired()]
                                )
