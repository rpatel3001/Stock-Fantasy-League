"""Main server appplication for the fantasy platform.

Provides routing for dynamic parts of the site, and links front-end API calls
to back-end database transactions.
"""

from urllib.parse import urlparse
import os
import sys
from flask import Flask
import pyrebase
import psycopg2
import psycopg2.extras
import stock_data


def debug(str):
    """Debug printing for Heroku."""
    print("==============================================", file=sys.stderr)
    print(str, file=sys.stderr)
    print("==============================================", file=sys.stderr)


app = Flask(__name__)

# init postgresql table
url = urlparse(os.environ["DATABASE_URL"])
db = psycopg2.connect(
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


@app.route('/')
def get_stock():
    """Landing page.

    Shows stored stock and it's current price.

    Args:
        none

    Raises:
        none

    Returns:
        string : text to be displayed as a website
    """
    db_conn = db.cursor()
    db_conn.execute("SELECT * FROM testdb WHERE name LIKE %s;", ('rajan',))
    user = db_conn.fetchone()
    db.commit()
    db_conn.close()
    try:
        return user['name'] + " has picked " + user['sym'] \
            + " which costs $" + stock_data.get_current_price(user['sym'])
    except ValueError:
        return "stored stock symbol " + user['sym'] + " was not found"


@app.route('/<string:user>/<string:stock>')
def set_stock(user, stock):
    """Update stored stock.

    Args:
        user (string) : The name of the user to update
        stock (string) : The new stock symbol to track

    Raises:
        none

    Returns:
        string : text to be displayed to the user as a web page
    """
    db_conn = db.cursor()
    db_conn.execute("UPDATE testdb SET sym = %s WHERE name = %s", (stock, user))
    success = db_conn.rowcount == 1
    db.commit()
    db_conn.close()
    if success:
        return user + "'s new stock is " + stock
    else:
        return "user not found"


if __name__ == "__main__":
    app.run(debug=True)
