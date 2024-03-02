# Using class-level and static methods

class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOKTYPES=("NEW","OLD","REFURBISHED")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOKTYPES

    # TODO: create a static method
    def getBookList():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title,booktype):
        self.title = title
        if(not booktype in self.BOOKTYPES):
            raise ValueError("Wrong book type")
        else:
            self.booktype = booktype


# TODO: access the class attribute

print(Book.getBookTypes())
# TODO: Create some book instances
b1=Book("Malala","NEW")
print(b1.booktype)
b2=Book("I Am Malala","OLD")
# TODO: Use the static method to access a singleton object
booksList=Book.getBookList()
booksList.append(b1)
booksList.append(b2)
