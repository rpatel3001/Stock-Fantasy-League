from flask_restful import reqparse, abort, Resource
import json

class updateUserInfo(Resource):
	@staticmethod
	def post(cur, UID):
		parser = reqparse.RequestParser()
		parser.add_argument('update')
		args = parser.parse_args()
		newInfo = json.loads(args['update'])
		cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'userprefs';")
		userColumns = cur.fetchall()
		userColumns = [x['column_name'] for x in userColumns]
		query = ''
		temp = ''
		for column in userColumns:
			if column == 'messages' or column == 'notifications':	#handler for json strings
				temp = str(column) + '=' + "'" +  json.dumps((newInfo[column])) + "'"
				query += temp + ","
				continue
			if column == 'lid' or column == 'pid':					#handler for arrays
				if newInfo[column] == None:
					temp = str(column) + '=' + "'{}'"
					query += temp + ","
					continue
				idList = [str(a) for a in newInfo[column]]
				idList = ", " . join(idList)
				temp = str(column) + "='{" + idList + "}'"
				query += temp + ","
				continue
			if column == 'username' or column == 'description' or column == 'imageurl' or column == 'email':	#handler for strings with spaces/symbols
				temp = str(column) + '=' + "'" + newInfo[column] + "'"
				query += temp + ","
				continue
			if column == 'friends':
				if newInfo[column] == None:
					temp = str(column) + '=' + "'{}'"
					query += temp + ","
				continue
			
			temp = str(column) + '=' + str(newInfo[column])
			query += temp + ","
			pass
		query = query[:-1]
		print(query)
		cur.execute("UPDATE userprefs SET %s WHERE uid = %s;"% (query, UID))

		return "Success"

