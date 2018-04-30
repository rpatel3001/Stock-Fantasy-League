from flask_restful import reqparse, abort, Resource

class leaveLeague(Resource):
	@staticmethod
	def patch(cur, PID):
		#when leaving, you have PID, which gives corresponding LID and UID,
			#save PID first, then LID, then UID
		cur.execute("SELECT lid, uid FROM players WHERE pid = %s;", [PID])
		stats = cur.fetchone()
		
		league = stats['lid']
		user = stats['uid']
		player = PID

		cur.execute("DELETE FROM players WHERE pid = %s", [PID])	#deletes player row from player table
		cur.execute("UPDATE leagues SET pid = array_remove(pid, %s), uid = array_remove(uid, %s) WHERE lid = %s;", (PID, user, league))
		cur.execute("UPDATE userprefs SET lid = array_remove(lid, %s), pid = array_remove(pid, %s) WHERE uid = %s;", (league, player, user))
		
		return "Left League"