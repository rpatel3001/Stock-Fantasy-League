from flask_restful import reqparse, abort, Resource
import json

class getALLPlayerInfoFromLID(Resource):
	@staticmethod
	def get(cur, LID):

		if LID < 7:
			cur.execute("SELECT pid FROM premade_leagues WHERE lid = %s;", [LID,])
		else:
			cur.execute("SELECT pid FROM leagues WHERE lid = %s;", [LID,])

		pidArray = cur.fetchone()

		if pidArray['pid'] == []:
			return "No players"
		else:			
			listofarrays = pidArray['pid']
			string = ", ".join( repr(e) for e in listofarrays)
			test = [int(s) for s in string.split(',')]
			cur.execute("SELECT * FROM players WHERE pid IN %s;", (tuple(test),))
			return cur.fetchall()
