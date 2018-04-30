from flask_restful import reqparse, abort, Resource

class leaveLeague(Resource):
	@staticmethod
	def patch(cur, PID):
		cur.execute("SELECT lid, uid FROM players WHERE pid = %s;", [PID])
		stats = cur.fetchone()
		
		league = stats['lid']
		user = stats['uid']
		player = PID
		
		if int(league) < 8:
			cur.execute("DELETE FROM players WHERE pid = %s", [PID])	#deletes player row from player table
			cur.execute("UPDATE premade_leagues SET pid = array_remove(pid, %s), uid = array_remove(uid, %s) WHERE lid = %s;", (PID, user, league))
			cur.execute("UPDATE userprefs SET lid = array_remove(lid, %s), pid = array_remove(pid, %s) WHERE uid = %s;", (league, player, user))
		else:
			cur.execute("DELETE FROM players WHERE pid = %s", [PID])	#deletes player row from player table
			cur.execute("UPDATE leagues SET pid = array_remove(pid, %s), uid = array_remove(uid, %s) WHERE lid = %s;", (PID, user, league))
			cur.execute("UPDATE userprefs SET lid = array_remove(lid, %s), pid = array_remove(pid, %s) WHERE uid = %s;", (league, player, user))
			pass

		

		# cur.execute("DELETE FROM players WHERE pid = %s", [PID])	#deletes player row from player table
		# cur.execute("UPDATE leagues SET pid = array_remove(pid, %s), uid = array_remove(uid, %s) WHERE lid = %s;", (PID, user, league))
		# cur.execute("UPDATE userprefs SET lid = array_remove(lid, %s), pid = array_remove(pid, %s) WHERE uid = %s;", (league, player, user))
		
		return "Left League"