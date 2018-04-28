from flask_restful import reqparse, abort, Resource

class buyVIP(Resource):
	def patch(cur, UID):
		#we're going to need some verification system in backend or front end to check
		cur.execute("UPDATE userprefs SET vip = true WHERE uid = %s;", [UID])
		return "VIP Bought"
		pass