from flask_restful import reqparse, abort, Resource

class LeagueHome(Resource):

    @staticmethod
    def get(cur, LID):
        return 'Hello, Brian, ID = ' + str(LID)