from flask_restful import reqparse, abort, Resource


class User(Resource):

    @staticmethod   #method to create a league
    def post(cur, UID): 
        parser = reqparse.RequestParser()
        parser.add_argument('startBal')
        parser.add_argument('duration')
        parser.add_argument('leagueName')
        parser.add_argument('description')
        args = parser.parse_args()
        cur.execute("INSERT INTO players (uid) VALUES (%s);", [UID])   #creates a player in the database with the creaters UID
        cur.execute("SELECT pid from players where uid=%s;", [UID])  #used to return PID to add into the leagues database
        createdPID = cur.fetchall() #sets equal to dictionary of PIDs
        cur.execute("INSERT INTO leagues (startBal, duration, leagueName, description, ownerUID, ownerPID) VALUES (%s, %s, %s, %s, %s, %s);", (float(args['startBal']), float(args['duration']), args['leagueName'], args['description'], UID, createdPID[-1]['pid']))   #creates the league with the user inputs
        cur.execute("SELECT lid from leagues WHERE ownerUID=%s", [UID]) #gets the leagueID from league table for the created table
        createdLID = cur.fetchall() #sets equal to dictionary of LIDs       
        cur.execute("UPDATE players SET lid = %s WHERE pid = %s;", (createdLID[-1]['lid'], createdPID[-1]['pid']))    #updates players table(add themselves into league)
        cur.execute("UPDATE userprefs SET lid = lid || %s WHERE uid = %s;", (createdLID[-1]['lid'], UID))   #updates user table (add themselves into league)
        cur.execute("UPDATE userprefs SET pid = pid || %s WHERE uid = %s;", (createdPID[-1]['pid'], UID))
        cur.execute("UPDATE leagues SET uid = uid || %s WHERE lid = %s;", (UID, (createdLID[-1]['lid'])))
        cur.execute("UPDATE leagues SET pid = pid || %s WHERE lid = %s;", (createdPID[-1]['pid'], createdLID[-1]['lid']))
        return createdLID
        pass
    
    @staticmethod   #method to get info for user (changed for AJAX messages)
    def get(cur, UID):
        cur.execute("SELECT * FROM userprefs WHERE uid = %s;", [UID])
        return cur.fetchone();
        pass
