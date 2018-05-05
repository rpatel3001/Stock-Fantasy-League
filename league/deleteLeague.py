from flask_restful import reqparse, abort, Resource

class deleteLeague(Resource):
	'''Deletes a usermade league'''
	@staticmethod
	def delete(cur, LID):
		""" 
        Args:
            lid (int) : the ID of the league

        Returns:
			"Deleted"
        """

		cur.execute("SELECT uid FROM leagues WHERE lid = %s;", [LID])
		usersFromLeagues = cur.fetchone()
		cur.execute("SELECT pid FROM leagues WHERE lid = %s;", [LID])
		playersFromLeagues = cur.fetchone()
		
		usersFromLeagues = usersFromLeagues['uid']
		playersFromLeagues = playersFromLeagues['pid']

		cur.execute("UPDATE userprefs SET lid = array_remove(lid, %s);", [LID])	#removes leagues from every user on user table
		for x in playersFromLeagues:
			cur.execute("UPDATE userprefs SET pid = array_remove(pid, %s);", [x])	#removes players from user table (dont need to specify because PIDs are unique)
			pass
		cur.execute("DELETE FROM players WHERE lid = %s;", [LID])
		cur.execute("DELETE FROM leagues WHERE lid = %s;", [LID])

		return "Deleted"

		pass