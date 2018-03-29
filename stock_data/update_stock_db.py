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
            strs += [(x['sym'], x['name'], x['price']) for x in data]
            sleep(1)

        for s in syms:
            fullsyms.remove(s)
        strs = ','.join(["('%s','%s',%s)" % x for x in strs])
        cur.execute("INSERT INTO stockdata (symbol, name, price) "
                    "VALUES %s "
                    "ON CONFLICT(symbol) DO UPDATE "
                    "SET name = excluded.name, "
                    "price = excluded.price;" % strs)
        cur.execute("DELETE FROM stockdata WHERE symbol in %s" % str(tuple(fullsyms)))
