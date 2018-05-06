STOCK MARKET FANTASY

-------Unit testing-------

To be be able to run the unit test file : unittest.sh
-heroku command line interface must be installed.
Once Heroku CLI is installed, run the command: heroku local
You will be shown a confirmation of gunicorn starting up.
This will be used to run our application locally using commands however, all of this is able to be done at our live website at http://stock-fantasy-league.herokuapp.com 

----------------------------------------------------------------------------------------

Open another terminal window and follow the instructions below.

-must make the bash file is executable
	- run: chmod -x unittest.sh
-run script in bash
	- run: sh /path/of/file

-------Execution order:-------

1-#create users <uid = 1>, <uid = 2>
2-#user1: create league
3-#user2: join league
4-#any user: get information of user1
SCRIPT SLEEPS FOR 2 SECONDS: to view changes in database
5-#system: update player 1 -> Changes balance to 50000
6-#system: update user 1: -> Update user1's VIP status from false to true
7-#ADMIN: get information of all users
8-#System: get data for stock given ticker
9-#system: get all question data for trivia show
10:#user: finish quiz with 3/7 questions correct and send information to database
11:#system: automatically update at 12:00 AM every day all user reputation points

Included are snapshots of the database before and after the update of users and players

-------Whats in the Output File?-------

The output file shows the RAW data from the update. In our code, we return information back to the system so that it understands what is going on. When we create users, we return the user ID for the system (uid). For and 'get' function, it returns a json string of the information from the database. For 'updates', we return a string for successfully updating. For stock data, we return a json string of the information that was grabbed from the AlphaVantage API. The questions are sent as a json string. It has all information necessary to allow a quick and synchronized quiz show for all user simultaneously. The last update call is run automatically at night and returns a confirmation message of "updated" if everything finishes running. 

-------EXTRA NOTES-------

Our code was modified slightly to allow user creation without the use of google authentication. In order to run the code locally, google authentication must be turned off. The functionality is the exact same. The only modification was to enter the fields that google would provide us, manually.