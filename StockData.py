"""
Provide data about securities that are tradeable on the fantasy platform.

This includes price data for various time periods at various intervals
for stocks, ETFs, and cryptocurrencies.
"""

from requests import get

_AV_URL = "https://www.alphavantage.co/query"


def get_current_price(ticker):
	"""
	Gets the current price of a security.
	"""

    args = {"function": "BATCH_STOCK_QUOTES",
            "symbols": [ticker.upper()],
            "apikey": "DEDSQFY460FDRASD"}
    data_json = get(_AV_URL, params=args).json()
    if list(data_json.keys())[0] == 'Error Message':
        return data_json
    else:
        data = list(data_json['Stock Quotes'])[0]
        return data['2. price']


def get_current_prices(tickers):
	"""
	Get the current price of each security in a list.
	"""

    tickers = [x.upper() for x in tickers]
    args = {"function": "BATCH_STOCK_QUOTES",
            "symbols": ','.join(tickers),
            "apikey": "DEDSQFY460FDRASD"}
    data_json = get(_AV_URL, params=args).json()
    if list(data_json.keys())[0] == 'Error Message':
        return data_json
    else:
        data = list(data_json['Stock Quotes'])
        return dict(zip(tickers, [x['2. price'] for x in data]))


def get_price_history(ticker, start, end, resolution):
	"""
	Get the price history of a security.
	"""

    pass


def get_technical_indicator(ticker, indicator, resolution, period):
	"""
	Get a technical indicator for a security.
	"""

    pass
