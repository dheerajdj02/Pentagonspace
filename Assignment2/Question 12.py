# Python program to convert time from 12 hours to 24-hour format

#Code

def convert12to24(time): 

    if time[-2:] == "AM" and time[:2] == "12": 
        return "00" + str1[2:-2] 
    elif time[-2:] == "AM": 
        return str1[:-2]     
    elif time[-2:] == "PM" and time[:2] == "12": 
        return time[:-2] 
    else: 
        return str(int(time[:2]) + 12) + time[2:8]

time = input("Enter the time in 12 hours format:")
print("The time is in 24-hour format ",convert12to24(time))
