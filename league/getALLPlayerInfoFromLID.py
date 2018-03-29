from flask_restful import reqparse, abort, Resource
import json

class getALLPlayerInfoFromLID(Resource):
	@staticmethod
	def get(cur, LID):
		parser = reqparse.RequestParser()
		cur.execute("SELECT pid FROM leagues WHERE lid = %s;", [LID])
		pidArray = cur.fetchone()
		listofarrays = pidArray['pid']
		string = ", ".join( repr(e) for e in listofarrays)
		test = [int(s) for s in string.split(',')]
		cur.execute("SELECT * FROM players WHERE pid IN %s;", (tuple(test),))
		return cur.fetchall()
		pass
		