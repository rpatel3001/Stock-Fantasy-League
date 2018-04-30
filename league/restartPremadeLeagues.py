from flask_restful import reqparse, abort, Resource

class restartPremadeLeagues(Resource):
	@staticmethod
	def post(cur):
		cur.execute("TRUNCATE TABLE premade_leagues RESTART IDENTITY;")
		cur.execute("INSERT INTO premade_leagues (industry) VALUES ('NASDAQ'), ('Materials'), ('Industrial'), ('Financial'), ('Healthcare'), ('Utilities');")
		return "Restarted"
		pass