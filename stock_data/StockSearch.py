"""Search the stock database by symbol or name."""

from flask_restful import Resource


class StockSearch(Resource):
    """Search the stock database by symbol or name."""

    def get(cur, begin):
        """Search the stock database by symbol or name."""
        begin = begin.upper() + '%'
        cur.execute("SELECT symbol, name FROM stockdata WHERE symbol LIKE %s or NAME LIKE %s;", (begin, begin))
        return {"stocks": cur.fetchall()}
