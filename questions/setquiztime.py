import time
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

# create a time string for 2:45 PM on this day
start_str = time.strftime("%m/%d/%Y") + " 00:00:00"
end_str = time.strftime("%m/%d/%Y ") + " 23:59:59"
start_ts = int(time.mktime(time.strptime(start_str, "%m/%d/%Y %H:%M:%S")))
start_ts = start_ts + 53100  # 2:45PM every day

# value = datetime.datetime.fromtimestamp(start_ts)
# print(value.strftime('%Y-%m-%d %H:%M:%S'))
# print(start_ts)
#   debug

# insert the time string into the database
cur.execute(
    "UPDATE premade_leagues SET quiztime = %s WHERE startbal = 10000;", (start_ts,))
