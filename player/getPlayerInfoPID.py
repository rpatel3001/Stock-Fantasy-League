from flask_restful import reqparse, abort, Resource

class getPlayerInfo(Resource):
	@staticmethod
	def get(cur, PID):
		cur.execute("SELECT * from players WHERE pid = %s;", [PID])
		return cur.fetchall()
		pass

		