from flask_restful import reqparse, abort, Resource

class getPlayerInfoByUID(Resource):
	'''get all players information based off of UID'''
	@staticmethod	# method to grab player UIDs given LID and UID
	def get(cur, LID, UID):
		""" 
        Args:
            lid (int) : the ID of the league
            uid (int) : the ID of the user

        Returns:
			"All player information where LID and UID match (should be one player)"
        """
		cur.execute("SELECT * from players WHERE lid = %s AND UID = %s", (LID, UID))
		return cur.fetchall()
		pass
		