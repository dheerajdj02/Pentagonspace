#Write a Python program to display a number with a comma separator.
def comma_separator(number):
    return ("{:,}".format(number))

input_val = int(input("Enter the number: "))
print("The entered number is:",input_val)
print("Formatted Number with comma separator", comma_separator(input_val))
                
