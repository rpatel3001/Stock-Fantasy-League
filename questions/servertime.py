from flask_restful import reqparse, abort, Resource
import time
import math

class servertime(Resource):
	def get(cur):
        """ Return the current server time."""
		ts = time.time()
		return math.trunc(ts)
		pass

