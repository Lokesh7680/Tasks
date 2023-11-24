import math 
user_ip = int(input("Enter number:"))

input=user_ip

if user_ip >0:
    sum=input
    while user_ip>0:
        user_ip-=1
        sum+=user_ip
    print("The sum is :" + str(sum))

print("The number entered by user is :" + str(input))
