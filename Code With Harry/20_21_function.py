class Yawar:

    def __init__(self, name):
        self.name = name

    def findGreater(self, a, b):
        print(self.name)
        if a > b:
            print("a is greater.")
        else:
            print("b is greater.")


newHardik = Yawar("Hardik")
newHardik.findGreater(30, 20)
