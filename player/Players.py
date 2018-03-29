from flask_restful import reqparse, abort, Resource


class Players(Resource):

    # Getting a list of PIDS from an associated UID, utilizing the userprefs table
    @staticmethod
    def get(cur, UID):
        cur.execute("SELECT PID FROM userprefs WHERE UID LIKE %s;", (args['UID'],))
        return cur.fetchall()




class Player(Resource):

    #When a player is removed/leaves from a league, update userprefs, leagues, and players tables.
    @staticmethod
    def update(cur, UID, PID):
        cur.execute("UPDATE usersprefs SET pid = array_remove(pid, PID) VALUES (%s);", (args['PID']))
        cur.execute("UPDATE leagues SET pid = array_remove(pid, PID) VALUES (%s);", (args['PID']))
        cur.execute("DELETE from players where pid = (PID) Values (%s);", args['PID'])
        return