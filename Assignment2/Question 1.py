#Given a two integer numbers return their product and if the product is greater than 1000, then return their sum

#Given:
#number1 = 20
#number2 = 30

#Expected Output:
#The result is 600

#Given:
#number1 = 40
#number2 = 30
#Expected Output:
#The result is 70

#code

number1 = 20
number2 = 30
def two_integer(number1, number2):
    product = number1 * number2
    if product > 1000:
        return number1 + number2
    else:
        return product
res = two_integer(number1, number2)
print("The Output is", res)
