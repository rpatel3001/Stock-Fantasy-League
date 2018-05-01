"""Provides data about the top stocks."""

from flask_restful import Resource


class TopStocks(Resource):
    """Get the top stocks."""

    def get(cur, num):
        """Return the top num stocks."""
        cur.execute("SELECT * FROM stockdata WHERE price is not NULL AND price != 0 ORDER BY volume LIMIT %s;", (num,))
        ss = cur.fetchall()
        return {"stocks": ss}
