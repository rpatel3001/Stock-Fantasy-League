from flask_restful import reqparse, abort, Resource
import json

class Leagues(Resource):

    @staticmethod  # getAllLeaguesInfo
    def get(cur):
        cur.execute("SELECT * FROM leagues ORDER BY lid;")
        usermade = cur.fetchall()
        cur.execute("SELECT * from premade_leagues ORDER BY lid;")
        premade = cur.fetchall()
        #leagues = cur.fetchall()

        return usermade + premade
        # return json.dumps({"Usermade Leagues": usermade} + {"Preamade Leagues": premade})


        # returning all json strings as one large json string


