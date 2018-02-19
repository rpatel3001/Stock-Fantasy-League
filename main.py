from flask import Flask
import pyrebase

app = Flask(__name__)

apikeyfile = open('apikey.txt', 'r')
apikey = apikeyfile.readline()
fbconfig = {
	"apiKey": apikey,
	"authDomain": "stock-fantasy-league.firebaseapp.com",
	"databaseURL": "https://stock-fantasy-league.firebaseio.com",
	"storageBucket": "stock-fantasy-league.appspot.com",
	"serviceAccount": "serviceaccountdetails.json"
}
firebase = pyrebase.initialize_app(fbconfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/')
def getstock():
	user = db.child("users").child("u1").get().val()
	return user['firstname'] + " has picked " + user['stock']

@app.route('/<string:user>/<string:stock>')
def setstock(user, stock):
	users = db.child("users").get()
	for u in users.each():
		if u.val()['firstname'] == user:
			db.child("users").child(u.key()).update({"stock":stock})
			return "updated " + u.val()['firstname'] + "'s stock to " + stock

	return "user not found"

if __name__ == "__main__":
	app.run(debug=True)