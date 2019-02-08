# learn_flask

## 说明

该仓库代码依照下列教程进行：
http://www.pythondoc.com/flask-mega-tutorial/index.html



## 当前进度

### 第一章：Hello World

不求甚解完成
执行 run.py 来运行应用程序，接着在你的网页浏览器上打开 http://localhost:5000 网址



### 第二章：模板

- 回顾：回顾了第一章操作

- 为什么我们需要模板：
  - `return` 中可以带上 html 代码，但是会非常难看
  - 模板可以让代码易于分离、扩充、整理

- 模板从天而降
  - 模板只是写了一个大部分标准的HTML页面，唯一的区别是有一些动态内容的在 `{{ … }}` 中
  - 新函数 `render_template()`
  - jinja2 引擎

- 模板中控制语句：
  - 如何使用 if 语句
  - `return render_template("index.html",title='Home',user=user)`
- 模板中的循环语句：
  - 如何使用 for 语句
  - 有一个包含多组信息的数据（如下例中的 `post`）,把这个数据 return 回去
  - `return render_template("index.html",title='Home',user=user,posts=posts)`
- 模板继承：
  - 让某个 html 文件从另一个 html 文件中继承
  - 例如本例中的 index.html 继承自 base.html
  - 疑问：return 中的 `render_template()` 是指向了 index.html，但是即使把被继承的 base.html 中的一部分代码删掉，也照样能够显示。继承的原理是什么？



### 第三章：web 表单

- 回顾
- 配置
  - Flask-WTF 是一个扩展，封装了 WTForms 并且恰当地集成进 Flask 中
    - Flask-WTF 需要进行配置
    - 有了配置文件，我们需要告诉 Flask 去读取以及使用它
  - Flaks-WTF 扩展只需要两个配置
    - `CSRF_ENABLED` 配置是为了激活跨站点请求伪造保护
    - `SECRET_KEY` 配置仅仅当 CSRF 激活的时候才需要，它用于建立一个加密的令牌，来验证表单
- 用户登录表单
  - 不太理解：在 Flask-WTF 中，表单表示成对象 Form 类的子类，一个表单子类简单地把表单的域定义成类的变量
  - 导入 `Form` 类
    ```py
    from flask_wtf import Form
    ...
    class LoginForm(Form)
    ```
  - `StringField` 是一个文本输入框，可以增加 validators 作为验证器
  - `BooleanField` 是一个单选框,`default` 字段表示默认是否勾选，`false` 为默认不勾选，同样可以增加 `validators` 作为验证器
  - `DataRequired` 验证器只是简单地检查相应域提交的数据是否是空
- 表单模板
  - `form.hidden_tag()` 模板参数将被替换为一个隐藏字段，用来是实现在配置中激活的 CSRF 保护。如果你已经激活了 CSRF，这个字段需要出现在你所有的表单中
  ```py
  <form action="" method="post" name="login">
    {{form.hidden_tag()}}
  ```
- 表单视图
  - 导入 `LoginForm` 类，从这个类实例化一个对象，接着把它传入到模板中，这就是我们渲染表单所有要做的事情
    ```py
    from .forms import LoginForm
    ...
    def login():
        form = LoginForm()
    ```
- 接收表单数据
  - `validate_on_submit()` 方法做了所有表单处理工作
    - `validate_on_submit` 在表单提交请求中被调用，它将会收集所有的数据，对字段进行验证
    - 验证通过，则返回 `True`，表示数据都是合法的
    - 当表单正在展示给用户的时候调用它，它会返回 `False`
    - 如果至少一个字段验证失败的话，它将会返回 `False`，接着表单会重新呈现给用户
  - `flash()` 函数可以在页面上快速展示数据，类似打印到页面的概念
  - `redirect()` 函数告诉网页浏览器引导到一个不同的页面而不是请求的页面
- 加强字段验证
  - 这一段运行没有报错，但是没有看到有错误信息，未得到验证
  - 通常情况下，任何需要验证的字段都会把错误信息放入 `form.field_name.errors` 下
    ```py
    <p>
        Please enter your OpenID:<br>
        {{ form.openid(size=80) }}<br>
        {% for error in form.openid.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}<br>
      </p>
    ```
- 处理 OpenIDs
  - 同样，代码运行没有报错，但是仍然看不到效果
- 其他问题
  - 多段重复代码放在一个文件中，用注释来切换运行的代码，仍然会因为重复的代码而受影响，尤其是 `extends` 和 `block xxx`|`endblock`这几块