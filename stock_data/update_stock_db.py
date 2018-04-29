"""Update the stock database data."""

from urllib.parse import urlparse
import os
import psycopg2
import psycopg2.extras
from requests import get
from datetime import date, timedelta
from time import sleep


def weekday():
    """String representation of the previous weekday."""
    adate = date.today() - timedelta(days=1)
    while adate.weekday() > 4:
        adate -= timedelta(days=1)
    return adate.strftime('%Y-%m-%d')


def chunk(n, iterable):
    """Util to iterate over a list in chunks."""
    args = [iter(iterable)] * n
    return zip(*args)


# init postgresql connection
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

u = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=DEDSQFY460FDRASD&symbol="

i = 0
with db_conn.cursor() as cur:
    cur.execute("SELECT symbol FROM stockdata;")
    fullsyms = [x['symbol'] for x in cur.fetchall()]

for sym in fullsyms:
    print(i, end='\r')
    i += 1
    sleep(.5)
    data = {'Information': 0}
    while True:
        data = get(u + sym).json()
        if 'Information' not in data.keys():
            break
        print(i)
        sleep(30)
    try:
        data = data['Time Series (Daily)']
        data = data[list(data.keys())[0]]
    except KeyError:
        print(sym)
        print(data)
        print()
        continue
    strs = "('%s', %s, %s)" % (sym, data['4. close'], data['5. volume'])
    with db_conn:
        with db_conn.cursor() as cur:
            cur.execute("INSERT INTO stockdata (symbol, price, volume) "
                        "VALUES %s "
                        "ON CONFLICT(symbol) DO UPDATE "
                        "SET price = EXCLUDED.price,"
                        "volume = EXCLUDED.volume;" % strs)
