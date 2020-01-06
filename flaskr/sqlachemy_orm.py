from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+mysqldb://root:root@localhost:3306/polls?charset=utf8", convert_unicode=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


def init_db():
    '''初始化数据库'''
    metadata.create_all(bind=engine)
