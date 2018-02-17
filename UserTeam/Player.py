'''
    TODO I don't think we need limitBuy and limitSell
'''


# For one stock, the stock info is stored in the following class
class stockInfo:
    def __init__(self, stockTicker, shares):
        self.stockTicker = stockTicker
        self.shares = shares

    # Return how many shares of a stock this person is holding
    def getShares(self):
        return self.holdings


class StockHolding:
    def __init__(self):
        # holds is an array of stocks a player is holding right now
        self.holds = []

    def buyStock(self, stockTicker, shares):
        # TODO add more conditions
        self.holds.append(stockInfo(stockTicker, shares))

    def sellStock(self, stockTicker, shares):
        holds = self.holds
        for i in holds:
            if i.stockTicker == stockTicker:
                # TODO add more conditions
                return 0
            else:
                print("The player does not own the stock selected.")
                return -1


class Player:
    def __init__(self, holding, fund=5000):
        self.holding = holding
        self.fund = fund

    def getHolding(self):
        return self.holding

    def marketBuy(self, sotckTicker, unitPrice, amount):
        if amount * unitPrice < self.fund:
            print("The player does not have enough money")
            return -1
        else:
            # TODO add the stock information into the field of holding
            return 0

    def marketSell(self, stockTicker, unitPrice, amount):
        return

    # TODO if the player does not hold enough shares

    def limitBuy(self, stockTicker, amount, limitPrice):
        if amount * limitPrice < self.fund:
            print("The player does not have enough money")
            return -1
        else:
            # TODO add the stock information into the field of holding
            return 0

    def limitSell(self, stockTicker, amount, limitPrice):
        return

    # TODO

    def shortBuy(self, stockTicker, amount, price):
        return

    # TODO

    def shortSell(self, stockTicker, amount, price):
        return
    # TODO
