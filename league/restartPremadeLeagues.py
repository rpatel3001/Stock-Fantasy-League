from flask_restful import reqparse, abort, Resource

class restartPremadeLeagues(Resource):
	@staticmethod
	def post(cur):
		cur.execute("TRUNCATE TABLE premade_leagues RESTART IDENTITY;")
		cur.execute("INSERT INTO premade_leagues (industry, description) VALUES ('NASDAQ', 'The NASDAQ is a market exchange allows investors to track stocks traded electronically. It contains different sectors for each industry.'), ('Materials', 'The basic materials sector is a category of stocks for companies involved in the discovery, development and processing of raw materials.'), ('Industrial', 'This sector includes companies involved with aerospace and defense, industrial machinery, tools, lumber production, construction, waste management, manufactured housing, cement and metal fabrication.'), ('Financial', 'The financial sector is a category of the economy made up of firms that provide financial services to commercial and retail customers. This sector includes banks, investment funds, insurance companies and real estate.'), ('Healthcare', 'The healthcare industry is the range of companies and non-profit organizations that provide medical services, manufacture medical equipment, and develop pharmaceuticals.'), ('Utilities', 'The utilities sector is a category of stocks for utilities such as gas and power. The sector contains companies such as electric, gas and water firms, and integrated providers.');")
		return "Restarted"
		pass