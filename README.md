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