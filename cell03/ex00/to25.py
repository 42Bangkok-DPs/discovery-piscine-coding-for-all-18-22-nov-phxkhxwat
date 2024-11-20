#!/usr/bin/env python3
print("Enter a number less than 25 ")
x = int(input())

if x >= 0 and x <= 25 :
    for i in range(x,26) :
        print("Inside the loop , my variable is  " ,x)
        x += 1
        
        

    
else :
    print("ERROR")