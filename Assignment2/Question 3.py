#Count all lower case, upper case, digits, and special symbols from a given string

#Given:

#str1 = "P@#yn26at^&i5ve"
#Expected Outcome:
#Total counts of chars, digits,and symbols
#Chars = 8
#Digits = 3
#Symbol = 4


def countUpperLowerNumberSymbols(inputValue):
    chars = 0
    number = 0
    symbol = 0
    for i in inputValue:
        if i >='A' and i <= 'Z' or i >= 'a' and i <= 'z':
            chars += 1
        elif i >='0' and i<= '9':
            number +=1
        else:
            symbol +=1

    print("Chars = ", chars)
    print("Digits = ", number)
    print("Symbol = ", symbol)

inputValue= "P@#yn26at^&i5ve"
countUpperLowerNumberSymbols(inputValue)
