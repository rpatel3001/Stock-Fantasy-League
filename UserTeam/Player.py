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

    def getStockTicker(self):
        return self.stockTicker




'''
    This object contains an array of "stockInfo" and is initialized as an empty list
'''
class StockHolding:
    def __init__(self):
        # holds is an array of stocks a player is holding right now
        self.holds = []

    # When the program restarts again, we might need to pull data from the database
    def pullHoldingDate(self, listOfHoldedStocks):
        self.holds = listOfHoldedStocks

    def findStock(self, stockTicker):
        if len(self.holds) == 0:
            return -1

        for i in range(len(self.holds)):
            if self.holds.getStockTicker == stockTicker:
                return i

        return -1


'''
   This class represents the actual player object which later will have the options of buying and selling
'''
class Player:
    def __init__(self, holding, fund=5000, PID):
        self.holding = StockHolding()
        # TODO We want to call pullHoldingDate() after the data base is ready
        self.balance = fund
        self.pID = PID

    def getHolding(self):
        return self.holding

    def getBalance(self):
        return self.balance



    def marketBuy(self, stockTicker, amount):
        if amount * getPrice(stockTicker) < self.getBalance():
            print("The player does not have enough money")
            return False
        else:
            index = self.holding.findStock(stockTicker)
            if index == -1:
                self.holding.append()


            # TODO add the stock information into the field of holding
            return True



    def marketSell(self, stockTicker, amount):




        if amount * getPrice(stockTicker) < self.getBalance():
            print("The player does not have enough stock shares")
            return False
        else:
            # TODO add the stock information into the field of holding
            return True

    # TODO if the player does not hold enough shares



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
