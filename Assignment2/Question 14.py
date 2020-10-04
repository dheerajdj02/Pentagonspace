#Python Program to Create a Class in which One Method Accepts a String from the User and Another print it


class User():
    def __init__(self):
        self.string=""
 
    def get(self):
        self.string=input("Enter string: ")
 
    def put(self):
        print("String is:")
        print(self.string)
 
String=User()
String.get()
String.put()
