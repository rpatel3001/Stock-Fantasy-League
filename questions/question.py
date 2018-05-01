from flask_restful import reqparse, abort, Resource
import json


class question(Resource):

    @staticmethod  # shows all users in database
    def get(cur,LID, PID):

        finalString = ""
        #cur.execute("SELECT * FROM questions_test;")
        ans1 = []
        for counter in range(1, 7):
            print(counter)
            cur.execute("SELECT * FROM question4 WHERE qid = %s;", (counter,))

            ans =cur.fetchall()
            for row in ans:
                ans1.append(dict(row))
            # finalString = finalString + cur.fetchone()
            print(ans1)


        """
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
        """
        return ans1