'''
通过声明的方式使用sqlachemy插件连接mysql

>>> from flaskr.sqlachemy_decl import init_db
>>> init_db()
>>> from flaskr.sqlachemy_decl import db_session
>>> from flaskr.model import User
>>> u = User('陈鹏', 'chenpeng@just.edu.cn')
>>> db_session.add(u)
>>> db_session.commit()
>>> quit()

'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+mysqldb://root:root@localhost:3306/polls?charset=utf8", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import flaskr.model
    Base.metadata.create_all(bind=engine)
