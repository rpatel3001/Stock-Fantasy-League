from flask_restful import reqparse, abort, Resource

class addquizpoints(Resource):
	@staticmethod
	def patch(cur, PID, score):
		currentPoints = cur.execute("SELECT quizpoints FROM players WHERE pid = %s;", [PID,])
		currentPoints = cur.fetchone()
		currentPoints = currentPoints['quizpoints']
		currentPoints += score 
		cur.execute("UPDATE players SET quizpoints = %s WHERE pid = %s;", (currentPoints, PID))

		return "Updated Score Successfully"		
		pass