from flask_restful import reqparse, abort, Resource
import json

class getlesson(Resource):
	@staticmethod
	def get(cur, lessonID):
		lesson = 'lesson_plan_' + str(lessonID)
		cur.execute("SELECT * from %s;" %lesson)
		lessonInfo = cur.fetchall();
		return lessonInfo