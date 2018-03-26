from flask_restful import reqparse, abort, Resource

class League(Resource):
    @staticmethod  # getLeagueInfo
    def get(cur, LID):
        """cmd = request.args.get('cmd')

        if cmd == "getLeaguesInfo":
            cur.execute("SELECT * from leagues where LID like %s;", LID)
            return cur.fetchone()
        else:
            return None
"""
