from flask_restful import reqparse, abort, Resource
import json

class getlesson(Resource):
	@staticmethod
	def get(cur, lessonID):
		""" 
        Args:
            lessonID (int) : the ID of the lesson

        Returns:
			"All information from lesson plan in json string format"
        """
		lesson = 'lesson_plan_' + str(lessonID)
		
		cur.execute("SELECT * from %s;" %lesson)
		lessonInfo = cur.fetchall();
		return lessonInfo