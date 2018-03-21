from flask_restful import reqparse, abort, Resource


class Player(Resource):
    pass















"""


'''
    TODO I don't think we need limitBuy and limitSell
'''


'''
    This is a fake method that I need to get from Rajan
'''
def getPrice(stockTicker):
    return



'''
    For one stock, the stock info is stored in the following class
'''
class stockInfo:
    def __init__(self, stockTicker, shares):
        self.stockTicker = stockTicker
        self.shares = shares

    # Return how many shares of a stock this person is holding
    def getShares(self):
        return self.shares

    def upDateShares(self, amount):
        self.shares += amount

    def getStockTicker(self):
        return self.stockTicker


'''
   This class represents the actual player object which later will have the options of buying and selling
'''
class Player:
    def __init__(self, PID, fund=5000):

        # holdings is an array of object --> stockInfo
        self.holdings = []

        # TODO We want to call pullHoldingDate() after the data base is ready

        self.balance = fund

        self.pID = PID

    # Return a list of stocks that have been held
    def getHolding(self):
        return self.holdings

    # Return current balance without counting the stock values
    def getBalance(self):
        return self.balance

    # When the program restarts again, we might need to pull data from the database
    def pullDate(self,  PID):

        #TODO
        return

        # Return the index of a stock in the list
    def findStock(self, stockTicker):
        if len(self.holdings) == 0:
            return -1

        for i in range(len(self.holdings)):
            if self.holdings[i].getStockTicker() == stockTicker:
                return i
            return -1


    def marketBuy(self, stockTicker, amount):
        if amount * getPrice(stockTicker) < self.getBalance():
            print("The player does not have enough money")
            return False
        else:
            index = self.findStock(stockTicker)
            if index == -1:
                self.holdings.append(stockInfo(stockTicker, amount))
            else:
                temp = self.holdings[index]
                temp.updateShares(amount)

            # Update the balance
            self.balance -= amount * getPrice(stockTicker)
            return True



    def marketSell(self, stockTicker, amount):
        index = self.findStock(stockTicker)
        if index == -1:
            print("The player does not have this stock.")
        elif amount > self.holdings[index]:
            print("The player does not have enough shares of this stock.")
        else:
            temp = self.holdings[index]
            temp.updateShares(amount * -1)
            # Update the balance
            self.balance += amount * getPrice(stockTicker)
            return True
        return False



    def limitBuy(self, stockTicker, amount):
        if amount * getPrice(stockTicker) < self.getBalance():
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


"""