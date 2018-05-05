from flask_restful import reqparse, abort, Resource
import time
import math

class servertime(Resource):
	def get(cur):
		""" 
        Args:
            None

        Returns:
			Server time in UNIX time
        """
		ts = time.time()
		return math.trunc(ts)
		pass

