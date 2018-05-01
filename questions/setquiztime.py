from flask_restful import reqparse, abort, Resource
import time
import datetime

class setquiztime(Resource):
	@staticmethod
	def post(cur):

		start_str = time.strftime( "%m/%d/%Y" ) + " 00:00:00"
		end_str = time.strftime( "%m/%d/%Y ") + " 23:59:59"
		start_ts = int( time.mktime( time.strptime( start_str, "%m/%d/%Y %H:%M:%S" ) ) )
		
		start_ts = start_ts + 53100	#2:45PM every day

		# value = datetime.datetime.fromtimestamp(start_ts)
		# print(value.strftime('%Y-%m-%d %H:%M:%S'))
		# print(start_ts)
		#	debug

		cur.execute("UPDATE premade_leagues SET quiztime = %s WHERE startbal = 10000;", (start_ts,))

		return "SET"
		


