#!/usr/bin/env python3

def main():
    print("Enter a number less than 25 ")
    x = int(input())

    if x >= 0 and x <= 25 :
        for i in range(x,26) :
            print("Inside the loop , my variable is  " ,i)
          
    else :
        print("ERROR")

if __name__ == "__main__" :
    main()