# Understanding multiple inheritance, classes that inherit from several others
class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name="class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name="class B"
#C inherits from A and B
class C(A,B):
    def __init__(self):
        super().__init__()
    def showProps(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)

c = C()
c.showProps()