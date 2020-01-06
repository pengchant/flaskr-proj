import os

from flask import Flask
from . import auth, blog, db, flask_redis_test, api_support
from .demo import HelloWorld
from .sqlachemy_decl import db_session


def create_app(test_config=None):
    '''创建一个app并配置这个app'''
    app = Flask(__name__, instance_relative_config=True)  # 第二个参数告诉app配置文件是相对路径
    app.config.from_mapping(
        SECRET_KEY="dev",  # it should be overridden with a random value when deploying.
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        # is the path where the SQLite database file will be saved
        REDIS_URL=flask_redis_test.REDIS_URL
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

    @app.teardown_appcontext
    def shutdown_session(exceptoin=None):
        '''flask will automatically remove database sessions at the end of the request'''
        db_session.remove()

    # 添加rest支持
    api_support.init_rest(app)
    # 测试helloworld
    api_support.api.add_resource(HelloWorld, '/helloworld')

    # 注册redis模块
    flask_redis_test.init_redis(app)

    # 注册数据库模块
    db.init_app(app)

    # 注册认证模块
    app.register_blueprint(auth.bp)

    # 注册blog模块
    app.register_blueprint(blog.bp)

    return app
