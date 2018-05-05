from flask_restful import reqparse, abort, Resource

class restartPremadeLeagues(Resource):
	@staticmethod
	def post(cur):
		""" 
        Args:
            None

        Returns:
			"Confirmation message saying that all of the premade leagues have been wiped and restarted"
        """
		cur.execute("TRUNCATE TABLE premade_leagues RESTART IDENTITY;")
		cur.execute("INSERT INTO premade_leagues (industry, description) VALUES ('NASDAQ', 'test'), ('Materials', 'test'), ('Industrial', 'test'), ('Financial', 'test'), ('Healthcare', 'test'), ('Utilities', 'test');")
		return "Restarted"
		pass