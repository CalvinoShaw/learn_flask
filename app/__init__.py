from flask import Flask

app = Flask(__name__)

# 告诉 Flask 去读取以及使用配置文件
app.config.from_object('config')
from app import views
