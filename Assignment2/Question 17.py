#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
input_value = input("Enter value: ")

n1 = input_value * 1
n2 = input_value * 2
n3 = input_value * 3
n4 = input_value * 4

total = int(n1) + int(n2) + int(n3) + int(n4)
print(total)
