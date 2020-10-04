#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


def uppers_lowers(string):
  uppers = 0
  lowers = 0
  for char in string:
    if char.islower():
      lowers += 1
    elif char.isupper():
      uppers +=1
    else: 
      pass
  print("Total number of upper case letters:",uppers)
  print("Total number of lower case letters:",lowers)

input_val = input("Enter string:")
print("Enterd string",input_val)
uppers_lowers(input_val)
