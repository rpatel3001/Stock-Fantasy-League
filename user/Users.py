from flask_restful import reqparse, abort, Resource
from flask import Flask, session, make_response, request
from google.oauth2 import id_token
from google.auth.transport import requests
import json


class Users(Resource):

    @staticmethod   #shows all users in database
    def get(cur):
        cur.execute("SELECT * FROM userprefs ORDER BY username ASC;")
        return json.dumps({"Users": cur.fetchall()})

    @staticmethod   #used to create account
    def post(cur):
        parser = reqparse.RequestParser()
        parser.add_argument('email')
        parser.add_argument('username')
        parser.add_argument('imageurl')
        parser.add_argument('token')
        args = parser.parse_args()

        token = args['token']
        idinfo = id_token.verify_oauth2_token(token, requests.Request())
        logintoken = idinfo['sub']  #aud is for website, sub is for the unique token

        cur.execute("SELECT uid FROM userprefs WHERE token LIKE %s;", (logintoken,))

        exists = cur.fetchone()

        if exists == None:  #when account does not exist
            cur.execute("INSERT INTO userprefs (email, username, imageurl, token) VALUES (%s,%s,%s,%s);", (args['email'], args['username'], args['imageurl'], logintoken))
            cur.execute("SELECT uid FROM userprefs WHERE token LIKE %s;", (logintoken,))
            userUID = cur.fetchone()
            
            if session.get('loginstatus') == None or session['loginstatus'] != logintoken:
                session["loginstatus"] = logintoken
            
            return userUID

        #when account exists in DB
        cur.execute("SELECT uid from userprefs WHERE token LIKE %s;", (logintoken,))
        newUserUID = cur.fetchone()
        cur.execute("UPDATE userprefs SET dailylogin = 1 WHERE uid = %s;", (newUserUID,))

        if session.get('loginstatus') == None or session['loginstatus'] != logintoken:
            session["loginstatus"] = logintoken
        return newUserUID
