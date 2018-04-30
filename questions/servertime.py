from flask_restful import reqparse, abort, Resource
import time;

class servertime(Resource):
	def get(cur):
		ts = time.time()
		return ts
		pass

