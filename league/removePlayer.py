from flask_restful import reqparse, abort, Resource
import json

class removePlayer(Resource):	#on the league page, if the OWNERUID is the users UID, include feature to remove a player
	@staticmethod
	def patch(cur, UID, LID, PID):
		cur.execute("SELECT * from leagues WHERE lid = %s;", [LID])
		owningUser = cur.fetchone()
		owningUser = owningUser['owneruid']	#gets the owning users ID number
		#check if the user trying to remove is the correct user
		if UID != owningUser:
			return "Error: You do not have the permissions to remove a player. [You are not the owner]"
			pass
		else:
			cur.execute("SELECT uid, lid FROM players WHERE pid = %s;", [PID]) #get league and user ID from the player table
			stats = cur.fetchone()
			league = stats['lid']
			user = stats['uid']
			cur.execute("DELETE FROM players WHERE pid = %s", [PID])	#deletes player row from player table
			cur.execute("UPDATE userprefs SET lid = array_remove(lid, %s), pid = array_remove(pid, %s) WHERE uid = %s;", (league, PID, user))
			cur.execute("UPDATE leagues SET pid = array_remove(pid, %s), uid = array_remove(uid, %s) WHERE lid = %s;", (PID, user, league))


		return "Player Removed"
		pass



		  