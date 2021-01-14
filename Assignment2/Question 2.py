#Reverse a given number and return true if it is the same as the original number

#Expected Output:
#original number 121
#The original and reverse number is the same

#original number 125
#The original and reverse number is not same

# Code

input_val = int(input('Enter number :'))
inp_val=input_val;
res = 0

while(input_val > 0): 
	a = input_val % 10
	res = res * 10 + a 
	input_val = input_val // 10
	
print('The reverse number is',res)

res_val=res;
if inp_val == res_val:
    print('The original and reverse number is the same')
else:
    print('The original and reverse number is not same')
