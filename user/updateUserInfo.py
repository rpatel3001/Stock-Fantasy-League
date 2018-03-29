from flask_restful import reqparse, abort, Resource
import json

class updateUserInfo(Resource):
	@staticmethod
	def post(cur, UID):
		parser = reqparse.RequestParser()
		parser.add_argument('update')
		args = parser.parse_args()
		newInfo = json.loads(args['update'])
		print(type(args['update']))
		print(type(newInfo))
		cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'userprefs';")
		userColumns = cur.fetchall()
		userColumns = [x['column_name'] for x in userColumns]
		query = ''
		temp = ''
		for column in userColumns:
			if column == 'messages' or column == 'notifications'
				temp = str(column) + '=' + "'" +  json.dumps((newInfo[column])) + "'"
				query += temp + ","
				continue
			
			temp = str(column) + '=' + str(newInfo[column])
			query += temp + ","
			pass
		query = query[:-1]
		cur.execute("UPDATE userprefs SET %s WHERE uid = %s;"% (query, UID))

		return "Success"