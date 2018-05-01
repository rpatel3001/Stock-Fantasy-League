from flask_restful import reqparse, abort, Resource

class updatepoints(Resource):
	"""used to update points every night at 12:00 AM"""
	@staticmethod
	def patch(cur):
		allPlayers = cur.execute("SELECT pid from players ORDER BY pid;")
		allPlayersList = cur.fetchall()
		playerList = [value['pid'] for value in allPlayersList]

		for player in playerList:
			userID = cur.execute("SELECT uid FROM players WHERE pid = %s;", [player,])	#returns the userID from player table which associates with PID
			userID = cur.fetchone()
			userID = userID['uid']	#now we have UID of player for this iteration of loop

			dailyLog = cur.execute("SELECT dailylogin FROM userprefs WHERE uid = %s;", (userID,))	#get daily login status
			dailyLog = cur.fetchone()
			dailyLog = dailyLog['dailylogin']

			count = cur.execute("SELECT logcount FROM userprefs WHERE uid = %s;", (userID,))
			count = cur.fetchone()
			count = count['logcount']











			if dailyLog == 1:
				count += 1
			else:
				count = 0;
			cur.execute("UPDATE userprefs SET logcount = %s;", count) #increment log count for consecutive days

		pass
		
		return "Updated"