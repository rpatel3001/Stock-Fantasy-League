"""Provides data about the top stocks."""

from flask_restful import Resource


class TopStocks(Resource):
    """Get the top stocks."""

    def get(cur, num):
        """Return the top num stocks."""
        cur.execute("SELECT * FROM stockdata limit %s;", (num,))
        return {"stocks": cur.fetchall()}
