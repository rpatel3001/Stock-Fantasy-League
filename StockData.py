"""Provide data about securities that are tradeable on the fantasy platform.

This includes price data for various time periods at various intervals
for stocks, ETFs, and cryptocurrencies.
"""

from requests import get

_AV_URL = "https://www.alphavantage.co/query"


def get_current_price(sym):
	"""Gets the current price of a security.

	Args:
		sym (string) : The symbol for the security whose price is requested.

	Raises:
		ValueError : If `sym` is not a symbol for a recognized security.
		Will also be raised when the AlphaVantage API is down.

	Returns:
		float : The price of the security represented by `sym`.
	"""

    args = {"function": "BATCH_STOCK_QUOTES",
            "symbols": [sym.upper()],
            "apikey": "DEDSQFY460FDRASD"}
    data_json = get(_AV_URL, params=args).json()
    if list(data_json.keys())[0] == 'Error Message':
        raise ValueError(data_json['Error Message'])
    else:
        data = list(data_json['Stock Quotes'])[0]
        return data['2. price']


def get_current_prices(tickers):
	"""Get the current price of each security in a list.

	Args:
		syms (string[]) : A list of symbols whose prices to report.

	Raises:
		ValueError : If any input symbol is not a valid symbol for a recognized security.
		Will also be raised when the AlphaVantage API is down.

	Returns:
		dict : A dictionary which maps the input symbols to their current price.
	"""

    tickers = [x.upper() for x in tickers]
    args = {"function": "BATCH_STOCK_QUOTES",
            "symbols": ','.join(tickers),
            "apikey": "DEDSQFY460FDRASD"}
    data_json = get(_AV_URL, params=args).json()
    if list(data_json.keys())[0] == 'Error Message':
        raise ValueError(data_json['Error Message'])
    else:
        data = list(data_json['Stock Quotes'])
        return dict(zip(tickers, [x['2. price'] for x in data]))


def get_price_history(sym, length, resolution):
	"""Get the price history of a security.

	Args:
		sym (string) : The symbol for the security whose price history is requested.
		length (int) : How far back to return data for, specified as a number of datapoints.
		resolution (string) : How far apart datapoints should be. Choose from "monthly", 
			"weekly", "daily", "60min", "30min", "15min", "5min", "1min". 

	Raises:
		ValueError : If `sym` is not a valid symbol for a recognized security, or if
			length is negative, or if resolution is not a valid value. 
			Will also be raised when the AlphaVantage API is down.

	Returns:
		dict : A dictionary of date strings to dictionaries containing open, high, low,
			and close prices as well as total volume for the period.
	"""

    pass


def get_technical_indicator(sym, indicator, resolution, window, price_type):
	"""Get a technical indicator for a security.

	Args:
		sym (string) : The symbol for the security whose indicator to return.
		indicator (string) : Which indicator to use. The full list is too long
			to include,	use the AlphaVantage API reference at
			https://www.alphavantage.co/documentation/
		resolution (string) : The time between datapoints.
		window (string) : The time window used in the calculation of the
			technical indicator.
		price_type (string) : Which price to use in the calculation: "close",
			"open", "high", "low".

	Raises:
		ValueError : If `sym` is not a valid symbol, or if `indicator`, `resolution`, 
			or `price_type` are not valid, or if window is negative. 

	Returns:
		dict : A dictionary of date strings to a dictionary mapping `indicator`
			to the indicator's value at the time indicated by the date string.
	"""

    pass
