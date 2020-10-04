#Generating random strings until a given string is generated

# Code

import string 
import random 
import time 
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'
input_val = input(str("Enter your string: ")) 
attemptThis = ''.join(random.choice(possibleCharacters)
                      for i in range(len(input_val)))
attemptNext = '' 
completed = False
iteration = 0
while completed == False: 
	print(attemptThis) 
	attemptNext = '' 
	completed = True
	for i in range(len(input_val)): 
		if attemptThis[i] != input_val[i]: 
			completed = False
			attemptNext += random.choice(possibleCharacters) 
		else: 
			attemptNext += input_val[i] 
	iteration += 1
	attemptThis = attemptNext 
	time.sleep(0.1)	
print("Input string matched " + str(iteration) + " iterations") 
