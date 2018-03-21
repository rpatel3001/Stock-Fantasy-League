from flask_restful import reqparse, abort, Resource

class Leagues(Resource):

    @staticmethod
    def get(cur, LID):
        return 'Hello, Brian, ID = ' + str(LID)