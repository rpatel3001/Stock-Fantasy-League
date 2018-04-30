from flask_restful import reqparse, abort, Resource
import json

class sendQuestion(Resource):
	@staticmethod
	def get(cur, QID):
		cur.execute("SELECT * from question WHERE qid = %s;", [QID])
		questionInfo = cur.fetchone();

		return questionInfo
		
		pass
