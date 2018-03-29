from flask_restful import reqparse, abort, Resource
import json

class updatePlayerInfo(Resource):
	@staticmethod
	def POST(cur, PID):
		parser = reqparse.RequestParser()
		parser.add_argument('update')
		args = parser.parse_args()

		newInfo = json.loads(args['update'])
		print(newinfo)

		return newInfo


		pass
