# Using the __str__ and __repr__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # # TODO: use the __str__ method to return a string
    def __str__(self) -> str:
        return f"{self.title} written by: {self.author} costs: ${self.price}"
    # TODO: use the __repr__ method to return an obj representation
    def __repr__(self) -> str:
        return f"{self.title},{self.author},{self.price}"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(str(b1))
print(repr(b2))
