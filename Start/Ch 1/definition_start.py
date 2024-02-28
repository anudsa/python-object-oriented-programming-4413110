# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions
# TODO: create a basic class that represents a book
class Book:
  def __init__(self,title):
    self.title = title
# TODO: create instances of the class // call the class name as a constructor function
libro1 = Book("1984")
libro2 = Book("un mundo feliz")
# TODO: print the class and property
print(libro1)
print(libro1.title)
print(libro2.title)
