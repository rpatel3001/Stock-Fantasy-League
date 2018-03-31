"""Collect company names and prices from a CSV downloaded from the NASDAQ website."""

from urllib.parse import urlparse
import psycopg2
import csv

url = urlparse("postgres://xqeuyuquhktxoq:c7869c5a14cb7f47eea6a586dbc23ffe5ee8522abfb2c3c4b2b0785db64b5916@ec2-54-243-239-66.compute-1.amazonaws.com:5432/den0hekga678pn")
db_conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cur = db_conn.cursor()

csvreader = csv.DictReader(open('companylist.csv'))
for row in csvreader:
    if(row['LastSale'] == "n/a"):
        continue
    print(row)
    print()
    cur.execute("INSERT INTO stockdata (symbol, name, price) VALUES(%s,%s,%s)", (row['Symbol'], row['Name'], row['LastSale']))
db_conn.commit()
