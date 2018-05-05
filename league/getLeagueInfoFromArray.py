from flask_restful import reqparse, abort, Resource

class getLeagueInfoFromArray(Resource):
	'''get all league information from league array'''
	@staticmethod
	def get(cur):
		""" 
        Args:
            lidarray (int[]) : the IDs of all leagues

        Returns:
			"All league information from the league table (from both the premades and the usermade leagues"
        """
		parser = reqparse.RequestParser()
		parser.add_argument("lidarray")
		args = parser.parse_args()
		listofarrays = args["lidarray"]
		test = [int(s) for s in listofarrays.split(',')]
		
		cur.execute("SELECT * FROM premade_leagues WHERE lid IN %s;", (tuple(test),))
		premade = cur.fetchall()

		cur.execute("SELECT * FROM leagues WHERE lid IN %s;", (tuple(test),))
		usermade = cur.fetchall()

		return premade + usermade
		pass

		

