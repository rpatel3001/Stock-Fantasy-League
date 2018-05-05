import math
from urllib.parse import urlparse
import os
import psycopg2

# connect to the database
try:
    url = urlparse(os.environ["DATABASE_URL"])
except:
    url = urlparse("postgres://xqeuyuquhktxoq:c7869c5a14cb7f47eea6a586dbc23ffe5ee8522abfb2c3c4b2b0785db64b5916@ec2-54-243-239-66.compute-1.amazonaws.com:5432/den0hekga678pn")
db_conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
    cursor_factory=psycopg2.extras.RealDictCursor
)
cur = db_conn.cursor()

allPlayers = cur.execute("SELECT pid from players ORDER BY pid;")
allPlayersList = cur.fetchall()
playerList = [value['pid'] for value in allPlayersList]
print("all players: " + str(playerList))

for player in playerList:
    print("For player" + str(player))
    # returns the userID from player table which associates with PID
    userID = cur.execute(
        "SELECT uid FROM players WHERE pid = %s;", [player, ])
    userID = cur.fetchone()
    # now we have UID of player for this iteration of loop
    userID = userID['uid']

    # get daily login status
    dailyLog = cur.execute(
        "SELECT dailylogin FROM userprefs WHERE uid = %s;", (userID,))
    dailyLog = cur.fetchone()
    dailyLog = dailyLog['dailylogin']

    count = cur.execute(
        "SELECT logcount FROM userprefs WHERE uid = %s;", (userID,))
    count = cur.fetchone()
    count = count['logcount']

    balance = cur.execute(
        "SELECT availbalance FROM players WHERE pid = %s;", [player, ])
    balance = cur.fetchone()
    balance = balance['availbalance']

    quizpoints = cur.execute(
        "SELECT quizpoints from players WHERE pid = %s;", [player, ])
    quizpoints = cur.fetchone()
    quizpoints = quizpoints['quizpoints']

    numberofholdings = cur.execute(
        "SELECT holdings FROM players WHERE pid = %s;", [player, ])
    numberofholdings = cur.fetchone()
    numberofholdings = numberofholdings['holdings']
    # now has the number of shares of each stock
    holdingListNums = [value['numberShares'] for value in numberofholdings]
    # now has the number of shares of each stock
    holdingListNames = [value['symbol'] for value in numberofholdings]

    totalUniqueHoldings = len(numberofholdings)  # number of unique shares
    # total number of shares of all stocks
    totalNumHoldings = sum(holdingListNums)
    shareValues = []
    for x in range(0, totalUniqueHoldings):
        cur.execute(
            "SELECT price FROM stockdata WHERE symbol = %s;", (holdingListNames[x],))
        price = cur.fetchone()
        price = price['price']
        shareValues.append(price*holdingListNums[x])
        pass
    totalShareValue = sum(shareValues)

    diverse = totalUniqueHoldings * (totalNumHoldings/10)

    # print("log in counter:" + str(count))
    # print("balance of account:" + str(balance))
    # print("quiz points:" + str(quizpoints))
    # print("number of shares:" + str(totalNumHoldings))
    # print("number of uniques:" + str(totalUniqueHoldings))
    # print("sharevalues:")

    score = math.pow(1.0685, count)
    score = score * ((balance+totalShareValue)/1000)
    score += (0.5 * quizpoints)
    score += diverse

    print("score: " + str(score))
    if dailyLog == 1:
        count += 1
    else:
        count = 0
    # increment log count for consecutive days
    cur.execute("UPDATE userprefs SET logcount = %s;", (count,))
    count = 0  # reset for next iteration

    cur.execute("UPDATE players SET reppoints = %s WHERE pid = %s;",
                (score, player))  # set points
