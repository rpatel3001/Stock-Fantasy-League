from flask_restful import reqparse, abort, Resource
import json
class League(Resource):
	@staticmethod  # getLeagueInfo
	#Getting league info from specified league
	def get(cur, LID):
		""" 
        Args:
            lid (int) : the ID of the league

        Returns:
			"All information pertaining to one league"
        """
		if LID < 7:
			cur.execute("SELECT * FROM premade_leagues WHERE lid = %s;", [LID])
			return cur.fetchall()
		else:
			cur.execute("SELECT * FROM leagues WHERE lid = %s;", [LID])
			return cur.fetchall()
	pass
 