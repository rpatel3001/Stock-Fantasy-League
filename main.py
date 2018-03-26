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
from user import Users, User
from player import Players
from league import Leagues, League
from StockData import StockData

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


@app.route('/users/')
def serve_users():
    """Serve users.html to the /users/ URL."""
    return app.send_static_file('users.html')


@app.route('/leagues/')
def serve_leagues():
    """Serve index.html to the root URL."""
    return app.send_static_file('leagues.html')

# add API endpoints
api.add_resource(class_with_db(Users.Users), '/api/user')
api.add_resource(class_with_db(User.User), '/api/user/<int:UID>')
api.add_resource(class_with_db(Players.Players), '/api/user/<int:UID>/player')
api.add_resource(class_with_db(Players.Player), '/api/user/<int:UID>/player/<int:PID>')
api.add_resource(class_with_db(Leagues.Leagues), '/api/league')
api.add_resource(class_with_db(League.League), '/api/league/<int:LID>')
api.add_resource(class_with_db(StockData.StockData), '/api/stock_data')


if __name__ == "__main__":
    app.run(debug=True)
