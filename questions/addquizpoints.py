from flask_restful import reqparse, abort, Resource

class addquizpoints(Resource):
	@staticmethod
	def patch(cur, PID, score):
		""" 
        Args:
            PID (int) : the ID of the player
            score (int) : the amount of points the player recieved during the quiz

        Returns:
			"Updated..." - database is updated with how many points the user has accumulated
        """
		currentPoints = cur.execute("SELECT quizpoints FROM players WHERE pid = %s;", [PID,])
		currentPoints = cur.fetchone()
		currentPoints = currentPoints['quizpoints']
		currentPoints += score 
		cur.execute("UPDATE players SET quizpoints = %s WHERE pid = %s;", (currentPoints, PID))

		return "Updated Score Successfully"		
		pass