from flask_restful import reqparse, abort, Resource

class UserHome(Resource):

    @staticmethod
    def get(cur, email,username,password):
        return 'Hello, Brian, ID = ' + str(UID)

    @staticmethod
    def post(cur, email, username, password):
        cur.execute("insert into userprefs (email, username, password) VALUES (%s,%s,%s)", (email,username,password));
        return