#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include a simple test function to test the class methods.

class inputoutput:
    def __init__(self):
        self.string = ""

    def get(self):
        self.string = input("Enter the value:")

    def print(self):
        print(self.string.upper())

stringObj = inputoutput()
stringObj.get()
stringObj.print()
