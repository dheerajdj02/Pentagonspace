#Write a Python program to check the validity of password input by users. 

#At least 1 letter between [a-z] and 1 letter between [A-Z].

#At least 1 number between [0-9].

#At least 1 character from [$#@].

#Minimum length of 6 characters.

#The maximum length of 16 characters.

#Code

import re

Password = input("Input your password:")
val = True

while val:  
    if (len(Password)<6 or len(Password)>16):
        break
    elif not re.search("[a-z]",Password):
        break
    elif not re.search("[0-9]",Password):
        break
    elif not re.search("[A-Z]",Password):
        break
    elif not re.search("[$#@]",Password):
        break
    elif re.search("\s",Password):
        break
    else:
        print("Valid Password")
        val=False
        break
if val:
    print("Not a Valid Password")
