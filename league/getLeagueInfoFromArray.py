from flask_restful import reqparse, abort, Resource

class getLeagueInfoFromArray(Resource):
	@staticmethod
	def get(cur):
		parser = reqparse.RequestParser()
		parser.add_argument('lidarray')
		args = parser.parse_args()
		listofarrays = args['lidarray']
		cur.execute("SELECT * FROM leagues WHERE lid IN %s;", (listofarrays))
		return cur.fetchall()
		pass

		

