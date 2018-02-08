from requests import get
import csv
import json
from datetime import date

# pull listing info for all stocks listed on NYSE, NASDAQ, and AMEX
stocks_csv = get("https://www.nasdaq.com/screening/companies-by-industry.aspx?&render=download").text

# contains only symbols for companies pulled above
syms = list(zip(*csv.reader(stocks_csv.splitlines())))[0][1:]
print("pulled %d tickers"%len(syms))

args = {"function" : "TIME_SERIES_DAILY_ADJUSTED",
		"symbol" : syms[0],
		"outputsize" : "compact",
		"apikey" : "DEDSQFY460FDRASD"}

print("pulling data for %s"%syms[0])

stock_json = get("https://www.alphavantage.co/query", params=args).json()["Time Series (Daily)"][date.today().strftime("%Y-%m-%d")]
print(json.dumps(stock_json, indent=4))