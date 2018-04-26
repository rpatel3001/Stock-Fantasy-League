from flask_restful import reqparse, abort, Resource
from flask import Flask, session, make_response, request
import json
import datetime


class question(Resource):

    @staticmethod  # shows all users in database
    def get(cur):

        finalString = ""

        #cur.execute("SELECT * FROM questions_test;")

        for counter in range(1, 10):
            cur.execute("SELECT question FROM questions_test WHERE id LIKE %s;", (counter))
            aQuestion = cur.fetchall()

            cur.execute("SELECT answer FROM questions_test WHERE id LIKE %s;", (counter))
            answerArray = cur.fetchall()

            cur.execute("SELECT additionalinfo FROM questions_test WHERE id LIKE %s;", (counter))
            additionalInfoArray = cur.fetchall()

            cur.execute("SELECT correct FROM questions_test WHERE id LIKE %s;", (counter))
            correctIndex = cur.fetchall()
            correctIndex = str(correctIndex)

            cur.execute("SELECT explanation FROM questions_test WHERE id LIKE %s;", (counter))
            explanation = cur.fetchall()

            finalString = finalString + "{" + "question:" + aQuestion + "," + "answer:" + answerArray + "," + "additionalInfo:" + additionalInfoArray + "," + "correctIndex:" + correctIndex + "," + "explanation:" + explanation + "}"

        time = datetime.datetime.now()

        finalString = "serverTime:" + time + "," + finalString
        return json.dumps({finalString})