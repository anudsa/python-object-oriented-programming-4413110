# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes
class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title,pages,price):
        self.title = title
        self.pages = pages
        self.price = price
        self.__secretNumberOfSales = 3.50
        # TODO: add properties
        self.getPrice()
    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    def setDiscount(self,discountPercentage):
        self._discount = discountPercentage
    def getSecret(self):
        return self.__secretNumberOfSales
# TODO: create some book instances
libro1 = Book("1984",120,9.99)
libro2 = Book("un mundo feliz",100,5.99)

# TODO: print the price of book1
#print(libro1.price)
print(libro1.getPrice())
print(libro2.getPrice())
# TODO: try setting the discount
#discount is applied
libro2.setDiscount(.5)
print(libro2.getPrice())
print(libro2._discount)
# TODO: properties with double underscores are hidden by the interpreter
print(libro1.getSecret())
print(libro2._Book__secretNumberOfSales)