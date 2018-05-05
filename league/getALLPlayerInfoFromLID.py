from flask_restful import reqparse, abort, Resource
import json

class getALLPlayerInfoFromLID(Resource):
	'''gets all PIDs from the league and gets all player info from that'''
	@staticmethod
	def get(cur, LID):
		""" 
        Args:
            lid (int) : the ID of the league

        Returns:
			json string of all info from player table for each player in the league
        """

		if LID < 7:
			cur.execute("SELECT pid FROM premade_leagues WHERE lid = %s;", [LID,])
		else:
			cur.execute("SELECT pid FROM leagues WHERE lid = %s;", [LID,])

		pidArray = cur.fetchone()

		if pidArray['pid'] == []:
			return "No players"
		else:			
			listofarrays = pidArray['pid']
			string = ", ".join( repr(e) for e in listofarrays)
			test = [int(s) for s in string.split(',')]
			cur.execute("SELECT * FROM players WHERE pid IN %s ORDER BY reppoints DESC;", (tuple(test),))
			return cur.fetchall()
