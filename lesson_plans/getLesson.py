from flask_restful import reqparse, abort, Resource
import json

class getLesson(Resource):
	@staticmethod
	def get(cur, lessonID):
		pass