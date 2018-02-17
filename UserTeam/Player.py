import numpy as np

'''
    TODO I don't think we need limitBuy and limitSell
'''


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
