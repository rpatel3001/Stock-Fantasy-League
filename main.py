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
from UserTeam.Users import Users
from UserTeam.User import User
from UserTeam.Players import Players
from LeagueTeam.Leagues import Leagues
from LeagueTeam.League import League
from testdir.testapp import UserStock

app = Flask(__name__)
api = Api(app)

# init postgresql connection
url = urlparse(os.environ["DATABASE_URL"])
db_conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
    cursor_factory=psycopg2.extras.DictCursor
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


api.add_resource(class_with_db(Users), '/api/user')
api.add_resource(class_with_db(User), '/api/user/<int:UID>') #deleting a UID, getting a single UID, modifying a single UID
api.add_resource(class_with_db(Players), '/api/user/<int:UID>/players') #getting the list of PID's associated with a UID, or modify(patch) when deleting a PID from UID
api.add_resource(class_with_db(Leagues), '/api/league') #creating a league, listing leagues
api.add_resource(class_with_db(League), '/api/league/<int: LID>') #deleting a league, getting a single league, modifying a single league


if __name__ == "__main__":
    app.run(debug=True)
