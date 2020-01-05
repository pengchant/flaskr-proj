import os

from flask import Flask
from . import auth, blog, db


def create_app(test_config=None):
    '''创建一个app并配置这个app'''
    app = Flask(__name__, instance_relative_config=True)  # 第二个参数告诉app配置文件是相对路径
    app.config.from_mapping(
        SECRET_KEY="dev",  # it should be overridden with a random value when deploying.
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
        # is the path where the SQLite database file will be saved
    )

    if test_config is None:
        # 加载这个实例的配置，如果存在
        app.config.from_pyfile('config.py', silent=True)  # when deploying, this can be used to set a real
    else:
        # 加载测试配置
        app.config.from_mapping(test_config)

    # 确定实例的文件夹存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # 注册数据库模块
    db.init_app(app)

    # 注册认证模块
    app.register_blueprint(auth.bp)

    # 注册blog模块
    app.register_blueprint(blog.bp)

    return app
