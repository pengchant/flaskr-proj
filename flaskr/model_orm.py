'''
通过Manual Object Relational Mapping的方式来连接mysql数据库
>>> from flaskr.sqlachemy_orm import init_db
>>> init_db()
>>> from flaskr.model_orm import Demo2
>>> init_db()
>>> u = Demo2('杨习贝', 'admin@hello')
>>> from flaskr.sqlachemy_orm import db_session
>>> db_session.add(u)
>>> db_session.commit()
'''

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

from flaskr.sqlachemy_orm import db_session, metadata


class Demo2(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Demo2 %r>' % (self.name)


users = Table('demo2', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(50), unique=True),
              Column('email', String(120), unique=True))

mapper(Demo2, users)
