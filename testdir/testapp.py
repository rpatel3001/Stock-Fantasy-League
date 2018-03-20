"""Define routes for test program."""

from flask_restful import reqparse, abort, Resource
from stock_data import stock_data


class UserStock(Resource):
    """Define routes for the test program."""

    @staticmethod
    def get(cur, user_name):
        """Landing page.

        Shows stored stock and it's current price.

        Args:
            none

        Raises:
            none

        Returns:
            string : text to be displayed as a website
        """
        cur.execute("SELECT * FROM testdb WHERE name LIKE %s;", (user_name,))
        user = cur.fetchone()
        if user is None:
            abort(404, message="User {} not found.".format(user_name))
        try:
            return {user['sym']: stock_data.get_current_price(user['sym'])}
        except ValueError:
            abort(404, message="Symbol {} not found.".format(user['sym']))

    @staticmethod
    def patch(cur, user_name):
        """Update stored stock.

        Args:
            user (string) : The name of the user to update
            stock (string) : The new stock symbol to track

        Raises:
            none

        Returns:
            string : text to be displayed to the user as a web page
        """
        parser = reqparse.RequestParser()
        parser.add_argument('stock_sym')
        args = parser.parse_args()
        sym = args['stock_sym']
        try:
            stock_data.get_current_price(sym)
        except ValueError:
            abort(404, message="Symbol {} not found".format(sym))

        cur.execute("UPDATE testdb SET sym = %s WHERE name = %s",
                    (sym, user_name))
        if cur.rowcount == 1:
            return {"message": "{}'s stock updated to {}".format(user_name, sym)}
        abort(404, message="User {} not found.".format(user_name))
