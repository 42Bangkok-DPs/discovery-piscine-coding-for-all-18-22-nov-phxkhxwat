#!/usr/bin/env python3
import math

def main():
    x = input("Give me a number: ")
    x = float(x)  

    if x.is_integer():  
        print(int(x))  
    else:
        x = math.ceil(x)  
        print(x)

if __name__ == "__main__" :
    main()
