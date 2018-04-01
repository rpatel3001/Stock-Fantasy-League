"""Collect company names and prices from a CSV downloaded from the NASDAQ website."""

from urllib.parse import urlparse
import psycopg2
import csv
import os

url = urlparse(os.environ["DATABASE_URL"])
db_conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

with db_conn:
    with db_conn.cursor() as cur:
        syms = []
        data = []
        csvreader = csv.DictReader(open('companylist.csv'))
        for row in csvreader:
            if row['LastSale'] == "n/a" or row['Symbol'] in syms:
                continue
            syms.append(row['Symbol'])
            data.append(str((row['Symbol'], row['Name'], float(row['LastSale']))))
        cur.execute("INSERT INTO stockdata (symbol, name, price) VALUES %s" % ','.join(data))
