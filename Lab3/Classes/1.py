class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string)
        print(self.string.upper())

bebrolino = StringManipulator()
bebrolino.getString()
bebrolino.printString()