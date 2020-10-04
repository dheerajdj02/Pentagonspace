#Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:


Amount = 0
while True:
    inp_val = input("Enter the Operation and then Amount :")
    if not inp_val:
        break
    values = inp_val.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        Amount+=amount
    elif operation=="W":
        Amount-=amount
    else:
        pass
print(Amount)
