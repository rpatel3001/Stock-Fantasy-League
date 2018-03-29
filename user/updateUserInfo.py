from flask_restful import reqparse, abort, Resource
import json


class updateUserInfo(Resource):
	
	@staticmethod
	def UPDATE(cur, UID):
		parser = reqparse.RequestParser()
		parser.add_argument('update')
		args = parser.parse_args()
		newInformation = args['update']
		# unfinished

		pass
		