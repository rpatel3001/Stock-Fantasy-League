from flask_restful import reqparse, abort, Resource


class User(Resource):

    @staticmethod   #method to create a league
    def post(cur, UID):
        parser = reqparse.RequestParser()
        parser.add_argument('startBal')
        # parser.add_argument('duration')
        # parser.add_argument('leagueName')
        # parser.add_argument('description')
        args = parser.parse_args()
        cur.execute("INSERT INTO leagues (startBal, owneruid) VALUES(%s, %s)", (args['startBal'], UID))
        # cur.execute("INSERT INTO leagues (uid, pid, startbal, duration, leaguename, description) VALUES(%s, %s, %s, DATE, %s, %s)", (UID, args['pid'], args['startBalance'], args['duration'], args['leagueName'], args['description']))
        cur.execute("SELECT lid FROM leagues where owneruid=%s;", [UID])

        return cur.fetchone()

    pass

    # to create league:
    # create a player
    # add a league to leagues in DB
    # put in CREATORS uid and lid
    # default starting balance
    # duration(make infinity an option)
    # league name`