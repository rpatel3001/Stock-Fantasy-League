from flask_restful import reqparse, abort, Resource
import math

class updatepoints(Resource):
	"""used to update points every night at 12:00 AM"""
	@staticmethod
	def patch(cur):
		""" 
        Args:
			NONE
        Returns:
			"Updated" - pulls data from all over every table the player is associated with and calculates point total for that day
        """
		allPlayers = cur.execute("SELECT pid from players ORDER BY pid;")
		allPlayersList = cur.fetchall()
		playerList = [value['pid'] for value in allPlayersList]
		print("all players: " + str(playerList))

		for player in playerList:
			print("For player" + str(player))
			userID = cur.execute("SELECT uid FROM players WHERE pid = %s;", [player,])	#returns the userID from player table which associates with PID
			userID = cur.fetchone()
			userID = userID['uid']	#now we have UID of player for this iteration of loop

			dailyLog = cur.execute("SELECT dailylogin FROM userprefs WHERE uid = %s;", (userID,))	#get daily login status
			dailyLog = cur.fetchone()
			dailyLog = dailyLog['dailylogin']

			count = cur.execute("SELECT logcount FROM userprefs WHERE uid = %s;", (userID,))
			count = cur.fetchone()
			count = count['logcount']

			balance = cur.execute("SELECT availbalance FROM players WHERE pid = %s;", [player,])
			balance = cur.fetchone()
			balance = balance['availbalance']

			quizpoints = cur.execute("SELECT quizpoints from players WHERE pid = %s;", [player,])
			quizpoints = cur.fetchone()
			quizpoints = quizpoints['quizpoints']

			numberofholdings = cur.execute("SELECT holdings FROM players WHERE pid = %s;", [player,])
			numberofholdings = cur.fetchone()
			numberofholdings = numberofholdings['holdings']
			holdingListNums = [value['numberShares'] for value in numberofholdings] 	#now has the number of shares of each stock
			holdingListNames = [value['symbol'] for value in numberofholdings] 	#now has the number of shares of each stock

			totalUniqueHoldings = len(numberofholdings) #number of unique shares
			totalNumHoldings = sum(holdingListNums)	#total number of shares of all stocks
			shareValues = []
			for x in range(0, totalUniqueHoldings):
				cur.execute("SELECT price FROM stockdata WHERE symbol = %s;", (holdingListNames[x],))
				price = cur.fetchone()
				price = price['price']
				shareValues.append(price*holdingListNums[x])
				pass
			totalShareValue = sum(shareValues)

			diverse = totalUniqueHoldings * (totalNumHoldings/10)

			# print("log in counter:" + str(count))
			# print("balance of account:" + str(balance))
			# print("quiz points:" + str(quizpoints))
			# print("number of shares:" + str(totalNumHoldings))
			# print("number of uniques:" + str(totalUniqueHoldings))
			# print("sharevalues:")



			score = math.pow(1.0685, count)
			score = score * ((balance+totalShareValue)/1000)
			score += (0.5 * quizpoints)
			score += diverse

			print("score: " + str(score))
			if dailyLog == 1:
				count += 1
			else:
				count = 0;
			cur.execute("UPDATE userprefs SET logcount = %s;", (count,)) #increment log count for consecutive days
			count = 0	#reset for next iteration

			cur.execute("UPDATE players SET reppoints = %s WHERE pid = %s;", (score, player))	#set points
		
		return "Updated"




