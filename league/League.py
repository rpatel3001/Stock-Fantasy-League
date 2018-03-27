from flask_restful import reqparse, abort, Resource
import json
class League(Resource):
    @staticmethod  # getLeagueInfo
    #Getting league info from specified league
    def get(cur, LID):

        cur.execute("SELECT uid, pid, startbal, leaguename, description, owneruid, ownerpid, type FROM leagues WHERE lid = %s;", [LID])
        # league = cur.fetchone()
        #
        # return "{'league':" + str(league) + "}"
        return json.dumps({"Leagues": cur.fetchall()})
        pass
