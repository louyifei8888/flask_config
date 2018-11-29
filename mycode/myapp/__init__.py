from flask import Flask

from myapp.ext import init_ext
from myapp.urls import init_api
from myapp.views import init_blue
from .settings import config


def create_app():
    app = Flask(__name__)
    # 配置
    app.config.from_object(config.get("debug"))
    # 初始化第三方
    init_ext(app)
    # 初始蓝图
    init_blue(app)

    init_api(app)
    return app