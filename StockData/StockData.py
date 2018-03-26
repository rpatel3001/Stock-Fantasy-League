"""Provide data about securities that are tradeable on the fantasy platform.

This includes price data for various time periods at various intervals
for stocks, ETFs, and cryptocurrencies.
"""

from requests import get as send_get
from flask import request
from flask_restful import abort, Resource

_AV_URL = "https://www.alphavantage.co/query"


class StockData(Resource):
    """Class that deals with the AlphaVantage API."""

    @staticmethod
    def get(cur):
        """Get the current price of each security in a list.

        Args:
            syms (string[]) : A list of symbols whose prices to report.

        Raises:
            ValueError : If any input symbol is not a valid symbol for a recognized
            security. Will also be raised when the AlphaVantage API is down.

        Returns:
            dict : A dictionary which maps the input symbols to their current price
        """
        cmd = request.args.get('cmd')
        tickers = [x.upper() for x in request.args.getlist('sym')]
        if len(tickers) == 0:
            abort(404, message="No tickers provided.")

        tickers = tickers[0].split(',')

        if cmd == "getStockData":
            return get_stock_data(cur, tickers)
        elif cmd == "getPriceHistory":
            return get_price_history(tickers[0])
        elif cmd == "getTechnicalIndicator":
            return get_technical_indicator(tickers)
        else:
            abort(404, message="Command " + cmd + " not supported.")


def get_stock_data(cur, tickers):
    """Get the current price of a security.

    Args:
        sym (string) : The symbol for the security whose price is requested.

    Raises:
        ValueError : If `sym` is not a symbol for a recognized security.
        Will also be raised when the AlphaVantage API is down.

    Returns:
        float : The price of the security represented by `sym`.
    """
    args = {"function": "BATCH_STOCK_QUOTES",
            "symbols": ','.join(tickers),
            "apikey": "DEDSQFY460FDRASD"}
    data_json = send_get(_AV_URL, params=args).json()
    if list(data_json.keys())[0] == 'Error Message':
        abort(404, message=data_json['Error Message'])
    response = []
    for s in data_json["Stock Quotes"]:
        sym = s["1. symbol"]
        cur.execute("SELECT name FROM stockdata WHERE symbol LIKE %s", (sym,))
        response.append({'sym': sym,
                         'price': s["2. price"],
                         'name': cur.fetchone()["name"]})
    return "{'data':" + str(response) + "}"


def get_price_history(sym, length, resolution):
    """Get the price history of a security.

    Args:
        sym (string) : The symbol for the security whose price history is
            requested.
        length (int) : How far back to return data for, specified as a number
            of datapoints.
        resolution (string) : How far apart datapoints should be. Choose from
            "monthly", "weekly", "daily", "60min", "30min", "15min", "5min",
            "1min".

    Raises:
        ValueError : If `sym` is not a valid symbol for a recognized security,
            or if length is negative, or if resolution is not a valid value.
            Will also be raised when the AlphaVantage API is down.

    Returns:
        dict : A dictionary of date strings to dictionaries containing open,
            high, low, and close prices as well as total volume for the period.
    """
    return "Endpoint not implemented."


def get_technical_indicator(sym, indicator, resolution, window, price_type):
    """Get a technical indicator for a security.

    Args:
        sym (string) : The symbol for the security whose indicator to return.
        indicator (string) : Which indicator to use. The full list is too long
            to include, use the AlphaVantage API reference at
            https://www.alphavantage.co/documentation/
        resolution (string) : The time between datapoints.
        window (string) : The time window used in the calculation of the
            technical indicator.
        price_type (string) : Which price to use in the calculation: "close",
            "open", "high", "low".

    Raises:
        ValueError : If `sym` is not a valid symbol, or if `indicator`,
            `resolution`, or `price_type` are not valid, or if window is
            negative.

    Returns:
        dict : A dictionary of date strings to a dictionary mapping `indicator`
            to the indicator's value at the time indicated by the date string.
    """
    return "Endpoint not implemented."
