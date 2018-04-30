from flask_restful import reqparse, abort, Resource
import json

class Leagues(Resource):

    @staticmethod  # getAllLeaguesInfo
    def get(cur):
        cur.execute("SELECT * FROM leagues;")
        usermade = cur.fetchall()
        cur.execute("SELECT * from premade_leagues;")
        premade = cur.fetchall()
        #leagues = cur.fetchall()
        return json.dumps({"Usermade Leagues": usermade} + {"Preamade Leagues": premade})
        #return "{'leagues':" + str(leagues) + "}"


        # returning all json strings as one large json string


