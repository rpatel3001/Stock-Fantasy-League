"""Main server appplication for the fantasy platform.

Provides routing for dynamic parts of the site, and links front-end API calls
to back-end database transactions.
"""

from urllib.parse import urlparse
from functools import wraps
import os
import sys
from flask import Flask
from flask_restful import reqparse, abort, Resource, Api
import pyrebase
import psycopg2
import psycopg2.extras
import stock_data


def debug(msg):
    """Debug printing for Heroku."""
    print("==============================================", file=sys.stderr)
    print(msg, file=sys.stderr)
    print("==============================================", file=sys.stderr)


def success(msg):
    """Return a success code."""
    return {"message": msg}, 200


app = Flask(__name__)
api = Api(app)

# init postgresql table
url = urlparse(os.environ["DATABASE_URL"])
db_conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
    cursor_factory=psycopg2.extras.DictCursor
)

# grab the firebase api key
API_KEY = os.environ["API_KEY"]

# grab the service account details and write them to a temporary file
FB_SERVICE_ACCOUNT_DETAILS = os.environ["FB_SERVICE_ACCOUNT_DETAILS"]
FB_SERVICE_ACCOUNT_DETAILS_FILE = open("serviceaccountdetails.json", 'w')
FB_SERVICE_ACCOUNT_DETAILS_FILE.write(FB_SERVICE_ACCOUNT_DETAILS)
FB_SERVICE_ACCOUNT_DETAILS_FILE.close()
FB_CONFIG = {
    "apiKey": API_KEY,
    "authDomain": "stock-fantasy-league.firebaseapp.com",
    "databaseURL": "https://stock-fantasy-league.firebaseio.com",
    "storageBucket": "stock-fantasy-league.appspot.com",
    "serviceAccount": "serviceaccountdetails.json"
}

# initialize firebase services
firebase = pyrebase.initialize_app(FB_CONFIG)
auth = firebase.auth()


def with_db(func):
    """Create a decorator to wrap functions which access the database."""
    @wraps(func)
    def wrapper(*a, **kw):
        """Using 'with' blocks commits transactions when the function exits."""
        with db_conn:
            with db_conn.cursor() as cur:
                return func(cur, *a, **kw)
    return wrapper


class UserStock(Resource):
    """Define routes for the test program."""

    @staticmethod
    @with_db
    def get(cur, user_name):
        """Landing page.

        Shows stored stock and it's current price.

        Args:
            none

        Raises:
            none

        Returns:
            string : text to be displayed as a website
        """
        cur.execute("SELECT * FROM testdb WHERE name LIKE %s;", (user_name,))
        user = cur.fetchone()
        if user is None:
            abort(404, message="User {} not found.".format(user_name))
        try:
            return {user['sym']: stock_data.get_current_price(user['sym'])}
        except ValueError:
            abort(404, message="Symbol {} not found.".format(user['sym']))

    @staticmethod
    @with_db
    def patch(cur, user_name):
        """Update stored stock.

        Args:
            user (string) : The name of the user to update
            stock (string) : The new stock symbol to track

        Raises:
            none

        Returns:
            string : text to be displayed to the user as a web page
        """
        parser = reqparse.RequestParser()
        parser.add_argument('stock_sym')
        args = parser.parse_args()
        sym = args['stock_sym']
        try:
            stock_data.get_current_price(sym)
        except ValueError:
            abort(404, message="Symbol {} not found".format(sym))

        cur.execute("UPDATE testdb SET sym = %s WHERE name = %s",
                    (sym, user_name))
        if cur.rowcount == 1:
            return success("{}'s stock updated to {}".format(user_name, sym))
        abort(404, message="User {} not found.".format(user_name))


api.add_resource(UserStock, '/<string:user_name>')

if __name__ == "__main__":
    app.run(debug=True)
