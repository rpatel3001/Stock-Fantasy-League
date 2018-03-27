from flask_restful import reqparse, abort, Resource
from flask import flask
from google.oauth2 import id_token
from google.auth.transport import requests


class Users(Resource):

    @staticmethod   #shows all users in database
    def get(cur):
        cur.execute("select * from userprefs;")
        return cur.fetchall()


    @staticmethod   #used to create account
    def post(cur):
        # parser = reqparse.RequestParser()
        # parser.add_argument('email')
        # parser.add_argument('username')
        # parser.add_argument('imageURL')
        # parser.add_argument('token')
        # args = parser.parse_args()

        args = request.getjson()


        token = args['token']
        idinfo = id_token.verify_oauth2_token(token, requests.Request())
        logintoken = idinfo['aud']
        cur.execute("SELECT uid FROM userprefs WHERE token LIKE %s;", (logintoken,))


        exists = cur.fetchone()

        if exists == None:
            cur.execute("INSERT INTO userprefs (email, username, imageurl, token) VALUES (%s,%s,%s,%s);", (args['email'], args['username'], args['imageurl'], logintoken))
            cur.execute("SELECT uid FROM userprefs WHERE token LIKE %s;", (logintoken,))
            return cur.fetchone()
            pass

        cur.execute("SELECT uid from userprefs WHERE token LIKE %s;", (logintoken,))
        return cur.fetchone()
