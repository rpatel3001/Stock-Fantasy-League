"""Generate quiz questions daily."""
import psycopg2
import psycopg2.extras
import os
from urllib.parse import urlparse
import string
import random
from requests import get


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
cur = db_conn.cursor()


# Question 1
q1 = "Which of these stock symbols is not real?"
cur.execute('SELECT symbol FROM stockdata ORDER BY RANDOM() LIMIT 2')
a11 = cur.fetchone()['symbol']
a12 = cur.fetchone()['symbol']
while True:
    a13 = ''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 4)))
    cur.execute("SELECT COUNT(*) FROM stockdata WHERE symbol LIKE '%s'" % a13)
    if cur.fetchone()['count'] == 0:
        break
print(q1)
print(a11)
print(a12)
print(a13)
print()


q2 = "Which of these stocks has the highest price?"
cur.execute('SELECT symbol, price FROM stockdata ORDER BY RANDOM() LIMIT 3')
u = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=DEDSQFY460FDRASD&symbol="
ans = []
for s in cur.fetchall():
    s = s['symbol']
    data = get(u + s).json()
    data = data['Time Series (Daily)']
    data = data[list(data.keys())[0]]
    ans.append((s, float(data['4. close'])))
ans = sorted(ans, key=lambda k: k[1])
a21 = ans[0][0]
a22 = ans[1][0]
a23 = ans[2][0]
print(q2)
print(a21)
print(a22)
print(a23)
print()


q3 = "Which of these stocks has the highest volume?"
cur.execute('SELECT symbol FROM stockdata ORDER BY RANDOM() LIMIT 3')
u = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=DEDSQFY460FDRASD&symbol="
ans = []
for s in cur.fetchall():
    s = s['symbol']
    data = get(u + s).json()
    data = data['Time Series (Daily)']
    data = data[list(data.keys())[0]]
    ans.append((s, int(data['5. volume'])))
ans = sorted(ans, key=lambda k: k[1])
a31 = ans[0][0]
a32 = ans[1][0]
a33 = ans[2][0]
print(q3)
print(a31)
print(a32)
print(a33)
print()


q4 = "Which of these stocks is doing historically well?"
cur.execute('SELECT symbol FROM stockdata ORDER BY RANDOM() LIMIT 3')
u = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=DEDSQFY460FDRASD&outputsize=full&symbol="
ans = []
for s in cur.fetchall():
    s = s['symbol']
    data = get(u + s).json()
    data = data['Time Series (Daily)']
    price = float(data[list(data.keys())[0]]['4. close'])
    keys = list(data.keys())[:253]
    data = [data[k] for k in keys]
    pmax = 0
    pmin = 1e100
    for d in data:
        pmax = max(pmax, float(d['2. high']))
        pmin = min(pmin, float(d['3. low']))
    rp = (price - pmin) / pmax
    ans.append((s, rp))
ans = sorted(ans, key=lambda k: k[1])
a41 = ans[0][0]
a42 = ans[1][0]
a43 = ans[2][0]
print(q4)
print(a41)
print(a42)
print(a43)
print()


q5 = "Which of these stocks belongs in the sector: "
sector = random.choice(("Utilities", "Health Care", "Financials", "Industrials", "Materials"))
q5 += sector + "?"
cur.execute("SELECT symbol FROM stockdata WHERE sector LIKE '%s' ORDER BY RANDOM() LIMIT 2" % sector)
a51 = cur.fetchone()['symbol']
a52 = cur.fetchone()['symbol']
cur.execute("SELECT symbol FROM stockdata WHERE sector NOT LIKE '%s' ORDER BY RANDOM() LIMIT 1" % sector)
a53 = cur.fetchone()['symbol']
print(q5)
print(a51)
print(a52)
print(a53)
print()


q6 = "Which of these stocks is most volatile?"
cur.execute('SELECT symbol FROM stockdata ORDER BY RANDOM() LIMIT 3')
u = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=DEDSQFY460FDRASD&outputsize=full&symbol="
ans = []
for s in cur.fetchall():
    s = s['symbol']
    data = get(u + s).json()
    data = data['Time Series (Daily)']
    price = float(data[list(data.keys())[0]]['4. close'])
    keys = list(data.keys())[:253]
    data = [data[k] for k in keys]
    pmax = 0
    pmin = 1e100
    for d in data:
        pmax = max(pmax, float(d['2. high']))
        pmin = min(pmin, float(d['3. low']))
    prange = (pmax - pmin) / pmax
    ans.append((s, prange))
ans = sorted(ans, key=lambda k: k[1])
a61 = ans[0][0]
a62 = ans[1][0]
a63 = ans[2][0]
print(q6)
print(a61)
print(a62)
print(a63)
print()
