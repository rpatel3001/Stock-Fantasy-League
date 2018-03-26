from flask_restful import reqparse, abort, Resource


class Users(Resource):

    @staticmethod   #shows all users in database
    def get(cur):
        cur.execute("select * from userprefs;")
        return cur.fetchall()


    @staticmethod   #used to create account
    def post(cur):
        parser = reqparse.RequestParser()

        parser.add_argument('email')
        parser.add_argument('username')
        parser.add_argument('imageURL')
        parser.add_argument('token')
        args = parser.parse_args()
        cur.execute("SELECT uid FROM userprefs WHERE token = %s;", (args['token']))
        exists = cur.fetchone()

        if exists == None:
            cur.execute("INSERT INTO userprefs (email, username, imageURL, token) VALUES (%s,%s,%s,%s);", (args['email'], args['username'], args['imageURL'], args['token']))
            cur.execute("SELECT uid FROM userprefs WHERE token = %s;", (args['token']))
            return cur.fetchone()
            pass

        cur.execute("SELECT uid from userprefs WHERE token = %s;", (args['token']))
        return cur.fetchone()




        # is account, log in - give old UID
        # isnt account  - create account, and give new UID
        # bad, return -1