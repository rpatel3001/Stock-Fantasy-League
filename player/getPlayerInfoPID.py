from flask_restful import reqparse, abort, Resource

class getPlayerInfoPID(Resource):
	@staticmethod
	def get(cur, PID):
		""" 
        Args:
            pid (int) : the ID of the player

        Returns:
			All information of the player given the PID
        """
		cur.execute("SELECT * from players WHERE pid = %s;", [PID])
		return cur.fetchall()
		pass

		