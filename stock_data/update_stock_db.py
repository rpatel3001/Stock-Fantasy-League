"""Update the stock database data."""

from urllib.parse import urlparse
import os
import psycopg2
import psycopg2.extras
from StockData import get_stock_data
from time import sleep


def chunk(n, iterable):
    """Util to iterate over a list in chunks."""
    args = [iter(iterable)] * n
    return zip(*args)


# init postgresql connection
url = urlparse(os.environ["DATABASE_URL"])
#url = urlparse("postgres://xqeuyuquhktxoq:c7869c5a14cb7f47eea6a586dbc23ffe5ee8522abfb2c3c4b2b0785db64b5916@ec2-54-243-239-66.compute-1.amazonaws.com:5432/den0hekga678pn")
db_conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
    cursor_factory=psycopg2.extras.RealDictCursor
)

syms = []
strs = []
with db_conn:
    with db_conn.cursor() as cur:
        cur.execute("SELECT symbol FROM stockdata;")
        fullsyms = [x['symbol'] for x in cur.fetchall()]

        for symchunk in chunk(100, fullsyms):
            data = get_stock_data(cur, symchunk)['stockdata']
            syms += [x['sym'] for x in data]
            strs += [(x['sym'], x['price'], x['volume']) for x in data]
            strlist = ','.join(["('%s', %s, %s)" % x for x in strs])
            print(cur.mogrify("INSERT INTO stockdata (symbol, price, volume) "
                        "VALUES %s "
                        "ON CONFLICT(symbol) DO UPDATE "
                        "SET price = excluded.price, "
                        "volume = excluded.volume;" % strlist))
            sleep(.5)
