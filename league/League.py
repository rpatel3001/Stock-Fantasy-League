from flask_restful import reqparse, abort, Resource
import json
class League(Resource):
	@staticmethod  # getLeagueInfo
	#Getting league info from specified league
	def get(cur, LID):
		if LID < 8:
			cur.execute("SELECT * FROM premade_leagues WHERE lid = %s;", [LID])
			return json.dumps({"Leagues": cur.fetchall()})
		else:
			cur.execute("SELECT uid, pid, startbal, leaguename, description, owneruid, ownerpid, type FROM leagues WHERE lid = %s;", [LID])
			return json.dumps({"Leagues": cur.fetchall()})
	pass
