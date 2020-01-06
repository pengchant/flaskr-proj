from flask_restful import Resource
from flaskr.api_support import api


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

