"""Main server appplication for the fantasy platform.

Provides routing for dynamic parts of the site, and links front-end API calls
to back-end database transactions.
"""

from urllib.parse import urlparse
from functools import wraps
import os
from flask import Flask
from flask_restful import Api
import psycopg2
import psycopg2.extras

from misc import Assistant
from user import Users, User, joinLeague, updateUserInfo, leaveLeague, buyVIP
from player import Players, getPlayerInfoPID, updatePlayerInfo
from league import Leagues, League, getPlayerInfoByUID, getLeagueInfoFromArray, getALLPlayerInfoFromLID, getEverythingLeague, deleteLeague, restartPremadeLeagues, removePlayer
from stock_data import StockData, TopStocks, StockSearch
from questions import question, sendQuestion
from lesson_plans import getLesson


app = Flask(__name__, static_url_path='')
api = Api(app)

# init postgresql connection
url = urlparse(os.environ["DATABASE_URL"])
db_conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
    cursor_factory=psycopg2.extras.RealDictCursor
)


def with_db(func):
    """Create a decorator to wrap functions which access the database."""
    @wraps(func)
    def wrapper(*a, **kw):
        """Using 'with' blocks commits transactions when the function exits."""
        with db_conn:
            with db_conn.cursor() as cur:
                return func(cur, *a, **kw)
    return wrapper


def class_with_db(cls):
    """Apply the 'with_db' decorator to all the functions in a class."""
    for attr in cls.__dict__:
        if callable(getattr(cls, attr)):
            setattr(cls, attr, staticmethod(with_db(getattr(cls, attr))))
    return cls


@app.route('/')
def serve_index():
    """Serve index.html to the root URL."""
    return app.send_static_file('index.html')

# add API endpoints
api.add_resource(class_with_db(question.question), '/api/league/<int:LID>/startquiz/<int:PID>')
api.add_resource(class_with_db(sendQuestion.sendQuestion), '/api/question/<int:QID>')

api.add_resource(class_with_db(buyVIP.buyVIP), '/api/user/<int:UID>/buyvip')
api.add_resource(class_with_db(Users.Users), '/api/user')   #GET: show all users || POST: create account
api.add_resource(class_with_db(User.User), '/api/user/<int:UID>')   #GET: user info given UID || POST: create a league
api.add_resource(class_with_db(updateUserInfo.updateUserInfo), '/api/user/<int:UID>/update')    #UPDATE: update user information
api.add_resource(class_with_db(joinLeague.joinLeague), '/api/user/<int:UID>/joinLeague')    #POST: join a league

api.add_resource(class_with_db(Players.Players), '/api/user/<int:UID>/player')  #GET: get list of PIDs given UID
api.add_resource(class_with_db(Players.Player), '/api/user/<int:UID>/player/<int:PID>') #UPDATE: when player leaves/is removed from league (looks unfinished?)
api.add_resource(class_with_db(updatePlayerInfo.updatePlayerInfo), '/api/player/<int:PID>/update')
api.add_resource(class_with_db(getPlayerInfoPID.getPlayerInfoPID), '/api/player/<int:PID>')

api.add_resource(class_with_db(Leagues.Leagues), '/api/league') #GET: get all leagues information
api.add_resource(class_with_db(League.League), '/api/league/<int:LID>') #GET: get league information for ONE LID
api.add_resource(class_with_db(getLeagueInfoFromArray.getLeagueInfoFromArray), '/api/league/multiple')   #GET: get all leagues given array of LIDs
api.add_resource(class_with_db(getPlayerInfoByUID.getPlayerInfoByUID), '/api/league/<int:LID>/user/<int:UID>')  #GET: get player info given UID and LID
api.add_resource(class_with_db(getALLPlayerInfoFromLID.getALLPlayerInfoFromLID), '/api/league/<int:LID>/getplayers')
api.add_resource(class_with_db(getEverythingLeague.getEverythingLeague), '/api/league/<int:LID>/everything')
api.add_resource(class_with_db(deleteLeague.deleteLeague), '/api/league/<int:LID>/delete') #deletes a league from league table (updates all tables accordingly)
api.add_resource(class_with_db(restartPremadeLeagues.restartPremadeLeagues), '/api/premade/restart') #restarts all premade leagues - trunacates and insertsld
api.add_resource(class_with_db(removePlayer.removePlayer), '/api/user/<int:UID>/league/<int:LID>/player/<int:PID>/remove')

api.add_resource(class_with_db(StockData.StockData), '/api/stock_data')
api.add_resource(class_with_db(TopStocks.TopStocks), '/api/stock_data/top/<int:num>')
api.add_resource(class_with_db(StockSearch.StockSearch), '/api/stock_data/search/<string:begin>')

api.add_resource(class_with_db(Assistant.Assistant), '/api/assistant')

app.secret_key='abc123'
#need to change to something more secure

if __name__ == "__main__":
    app.run(debug=True)

