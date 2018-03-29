from flask_restful import reqparse, abort, Resource

class getLeagueInfoFromArray(Resource):
	@staticmethod
	def get(cur):
		parser = reqparse.RequestParser()
		parser.add_argument("lidarray")
		args = parser.parse_args()
		listofarrays = args["lidarray"]
		test = [int(s) for s in listofarrays.split(',')]
		cur.execute("SELECT * FROM leagues WHERE lid IN %s;", (tuple(test),))
		return cur.fetchall()
		pass