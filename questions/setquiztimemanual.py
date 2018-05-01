from flask_restful import reqparse, abort, Resource
import time
import datetime

class setquiztimemanual(Resource):
	@staticmethod
	def post(cur):

		timestamp = time.time()

		timestamp = timestamp + 15	#set 15 seconds later


		cur.execute("UPDATE premade_leagues SET quiztime = %s WHERE startbal = 10000;", (timestamp,))

		return "SET"
		


