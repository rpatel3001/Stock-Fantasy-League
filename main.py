"""Main server appplication for the fantasy platform.

Provides routing for dynamic parts of the site, and links front-end API calls
to back-end database transactions.
"""

from flask import Flask
import pyrebase
import stock_data

app = Flask(__name__)

API_KEY_FILE = open('apikey.txt', 'r')
API_KEY = API_KEY_FILE.readline()
API_KEY_FILE.close()
FB_CONFIG = {
    "apiKey": API_KEY,
    "authDomain": "stock-fantasy-league.firebaseapp.com",
    "databaseURL": "https://stock-fantasy-league.firebaseio.com",
    "storageBucket": "stock-fantasy-league.appspot.com",
    "serviceAccount": "serviceaccountdetails.json"
}
firebase = pyrebase.initialize_app(FB_CONFIG)
auth = firebase.auth()
db = firebase.database()


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
    user = db.child("users").child("u1").get().val()
    try:
        return user['firstname'] + " has picked " + user['stock'] \
            + " which costs $" + stock_data.get_current_price(user['stock'])
    except ValueError:
        return "stored stock symbol " + user['stock'] + " was not found"


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
    users = db.child("users").get()
    for user_entry in users.each():
        if user_entry.val()['firstname'] == user:
            db.child("users").child(user_entry.key()).update({"stock": stock})
            return user_entry.val()['firstname'] + "'s new stock is " + stock

    return "user not found"


if __name__ == "__main__":
    app.run(debug=True)
