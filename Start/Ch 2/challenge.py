# Programming challenge: use inheritance and abstract classes
# Challenge: create a class structure to represent stocks and bonds
# Requirements:
# -- Both stocks and bonds have a price
# -- Stocks have a company name and ticker
# -- Bonds have a description, duration, and yield
# -- You should not be able to instantiate the base class
# -- Subclasses are required to override getDescription()
# -- getDescription returns formats for stocks and bonds
# For stocks: "Ticker: Company -- $Price"
# For bonds: "description: duration'yr' : $price : yieldamt%"
#Since both stocks and bonds are assets, this one is the superclass.
from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self,price):
        #We initialize the super class (abc)
        super().__init__()
        self.price=price

    @abstractmethod
    def getDescription():
        pass


class Stock(Asset):
    def __init__(self,ticker,price,company):
        super().__init__(price)
        self.company=company
        self.ticker=ticker
    def getDescription(self):
        return f"{self.ticker}: {self.company} -- {self.price}"

class Bond(Asset):
    def __init__(self, price,description,duration,yieldPercentage):
        super().__init__(price)
        self.description=description
        self.duration=duration
        self.yieldPercentage=yieldPercentage
    def getDescription(self):
        return f"{self.description}: {self.duration} yr: ${self.price}: {self.yieldPercentage}%"

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
try:
   ast = Asset(100.0)
except:
   print("Can't instantiate Asset!")

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

us30yr = Bond(95.31, "30 Year US Treasury", 30, 4.38)
us10yr = Bond(96.70, "10 Year US Treasury", 10, 4.28)
us5yr = Bond(98.65, "5 Year US Treasury", 5, 4.43)
us2yr = Bond(99.57, "2 Year US Treasury", 2, 4.98)

print(msft.getDescription())
print(goog.getDescription())
print(meta.getDescription())
print(amzn.getDescription())

print(us30yr.getDescription())
print(us10yr.getDescription())
print(us5yr.getDescription())
print(us2yr.getDescription())
