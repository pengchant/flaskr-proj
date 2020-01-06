from flask_redis import FlaskRedis

REDIS_URL = "redis://:@localhost:6379/0"

redis_store = FlaskRedis()


def init_redis(app):
    '''初始化redis'''
    redis_store.init_app(app)


class RedisClient:
    '''自定义redis封装'''

    @classmethod
    def get(self, key):
        return redis_store[key]

    @classmethod
    def set(clsself, key, value):
        redis_store[key] = value
