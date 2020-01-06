from flask_restful import Api

api = None


def init_rest(app):
    '''初始化rest'''
    global api
    api = Api(app)
