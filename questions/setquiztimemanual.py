from flask_restful import reqparse, abort, Resource
import time
import datetime

class setquiztimemanual(Resource):
	@staticmethod
	def get(cur):
		""" 
        Args:
            None	

        Returns:
			"SET" - sets quiz time to be 15 seconds after calling this function
        """
		timestamp = time.time()

		timestamp = timestamp + 15	#set 15 seconds later

class setquiztimemanual(Resource):
    @staticmethod
    def get(cur):
        # create a timestring for 15 seconds from the current time
        timestamp = time.time()
        timestamp = timestamp + 15  # set 15 seconds later

    # insert the time string into the database
        cur.execute(
            "UPDATE premade_leagues SET quiztime = %s WHERE startbal = 10000;", (timestamp,))

        return "SET"
