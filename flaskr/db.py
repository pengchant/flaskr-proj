import sqlite3

import click
from flask import g, current_app
from flask.cli import with_appcontext


def init_app(app):
    app.teardown_appcontext(close_db)  # 告诉Flask在返回响应后进行清理时调用这个函数。
    app.cli.add_command(init_db_command)  # 添加新的命令


def get_db():
    '''获取数据'''
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],  # current_app points to the Flask application
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row  # tells the connection to return rows that behave like dicts.

    return g.db


def close_db(e=None):
    '''关闭数据库'''
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    '''初始化数据库'''
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command("init-db")
@with_appcontext
def init_db_command():
    '''清除已经存在的数据并且创建新的表格'''
    init_db()
    click.echo("初始化数据库.")
