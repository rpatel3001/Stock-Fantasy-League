from flask_restful import reqparse, abort, Resource
import json
import time

class serverTime(Resource):

    @staticmethod  # shows all users in database
    def get(cur,LID, PID):

    	return (time.time())