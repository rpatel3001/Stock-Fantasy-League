from flask_restful import reqparse, abort, Resource

class getPlayerInfo(Resource):
	
	@staticmethod	# method to grab player UIDs given LID and UID
	def get(cur, LID, UID):
		cur.execute("SELECT pid from players WHERE lid = %s AND UID = %s", (LID, UID))
		return cur.fetchall()
		pass
		