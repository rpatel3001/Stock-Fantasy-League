from flask_restful import reqparse, abort, Resource

class getEverythingLeague(Resource):
	@staticmethod
	def get(cur, LID):
		cur.execute("SELECT userprefs.uid, userprefs.lid, userprefs.pid, userprefs.friends, userprefs.email, userprefs.messages, userprefs.notifications, userprefs.username, userprefs.imageurl, userprefs.vip, userprefs.description, players.pid, players.uid, players.lid, players.holdings, players.notifications, players.availbalance, players.pendingorders, players.translog FROM players INNER JOIN userprefs ON players.uid = userprefs.uid WHERE players.lid = %s;", (LID,))
		return cur.fetchall()
		