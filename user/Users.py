from flask_restful import reqparse, abort, Resource


class Users(Resource):

    @staticmethod
    def get(cur):
        cur.execute("select * from userprefs;")
        return cur.fetchall()


    @staticmethod
    def post(cur):
        parser = reqparse.RequestParser()

        parser.add_argument('email')
        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()

        cur.execute("insert into userprefs (email, username, password) VALUES (%s,%s,%s);", (args['email'], args['username'], args['password']))
        cur.execute("select UID from userprefs where email like %s;", (args['email'],))
        return cur.fetchone()