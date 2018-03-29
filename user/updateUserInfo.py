from flask_restful import reqparse, abort, Resource
import json

class updateUserInfo(Resource):
	
	@staticmethod
	def get(cur, UID):
		parser = reqparse.RequestParser()
		parser.add_argument('update')
		args = parser.parse_args()
		#used for debug
		# cur.execute("SELECT * FROM userprefs WHERE uid = %s;", ([UID]))
		# jsonINPUT = cur.fetchall() # =args['update']
		# for row in jsonINPUT:
		# print("new information")
		# print(newInformation)
		# print("keys")
		# print(newInformation.keys())
		# cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'userprefs';")
		# columns = cur.fetchall()
		# print("columns")
		# print(columns)
		# for column_name in newInformation.keys():
		# 	toBeUpdated.append(columns)
		# 	pass
		jsonstring = args['update']
		print("jsonstring")
		print(type(jsonstring))

		# if (newInformation['uid']) == None:
		# 	pass
		# else:
		# 	# cur.execute("UPDATE userprefs SET uid = %s WHERE uid = %s;", [UID], (newInformation['uid']))
		# 	print(newInformation['uid'])
		# 	pass


		# for row in newInformation
		# 	print(row['uid'])
		# 	cur.execute("UPDATE userprefs SET uid = %s WHERE uid = %s;", [UID], (newInformation['uid']))
		# 	print(row['lid'])
		# 	cur.execute("UPDATE userprefs SET lid = %s WHERE uid = %s;", [UID], (newInformation['lid']))
		# 	print(row['pid'])
		# 	cur.execute("UPDATE userprefs SET pid = %s WHERE uid = %s;", [UID], (newInformation['pid']))
		# 	print(row['friends'])
		# 	cur.execute("UPDATE userprefs SET friends = %s WHERE uid = %s;", [UID], (newInformation['friends']))
		# 	print(row['email'])
		# 	cur.execute("UPDATE userprefs SET email = %s WHERE uid = %s;", [UID], (newInformation['email']))
		# 	print(row['messages'])
		# 	cur.execute("UPDATE userprefs SET messages= %sWHERE uid = %s;", [UID], (newInformation['messages']))
		# 	print(row['notifications'])
		# 	cur.execute("UPDATE userprefs SET notifications= %s WHERE uid = %s;", [UID], (newInformation['notifications']))
		# 	print(row['username'])
		# 	cur.execute("UPDATE userprefs SET username = %s WHERE uid = %s;", [UID], (newInformation['username']))
		# 	print(row['imageurl'])
		# 	cur.execute("UPDATE userprefs SET imageurl = %s WHERE uid = %s;", [UID], (newInformation['imageurl']))
		# 	print(row['vip'])
		# 	cur.execute("UPDATE userprefs SET vip= %s WHERE uid = %s;", [UID], (newInformation['vip']))
		# 	print(row['token'])
		# 	cur.execute("UPDATE userprefs SET token = %s WHERE uid = %s;", [UID], (newInformation['token']))
		# 	print(row['description'])
		# 	cur.execute("UPDATE userprefs SET description = %s WHERE uid = %s;", [UID], (newInformation['description']))

		# 	pass


		return jsonstring

		pass
		
