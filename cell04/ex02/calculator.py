#!/usr/bin/env python3

def main():
    x = input("Give me the first number: ")
    y = input("Give me the second number: ")

    x = int(x)
    y = int(y)

    print("Thank you!")

    print(x ,"+",y,"=",x+y)
    print(x ,"-",y,"=",x-y)
    print(x ,"/",y,"=",x/y)
    print(x ,"*",y,"=",x*y)

if __name__ == "__main__":
    main()