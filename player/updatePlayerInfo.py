from flask_restful import reqparse, abort, Resource
import json

class updatePlayerInfo(Resource):
	@staticmethod
	def post(cur, PID):
		parser = reqparse.RequestParser()
		parser.add_argument('update')
		args = parser.parse_args()
		newInfo = json.loads(args['update'])
		cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'players';")
		playerColumns = cur.fetchall()
		playerColumns = [x['column_name'] for x in playerColumns]
		query = ''
		temp = ''
		for column in playerColumns:
			if column == 'holdings' or column == 'notifications' or column == 'pendingorders' or column == 'translog':
				temp = str(column) + '=' + "'" +  json.dumps((newInfo[column])) + "'"
				query += temp + ","
				continue
			
			temp = str(column) + '=' + str(newInfo[column])
			query += temp + ","
			pass
		query = query[:-1]
		cur.execute("UPDATE players SET %s WHERE pid = %s;"% (query, PID))

		return "Success"
