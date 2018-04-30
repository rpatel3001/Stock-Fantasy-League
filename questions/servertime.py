from flask_restful import reqparse, abort, Resource
import time
import math

class servertime(Resource):
	def get(cur):
		ts = time.time()
		return math.trunc(ts)
		pass

