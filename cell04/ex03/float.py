#!/usr/bin/env python3

def main():
    x =input("Give me a number: ")
    num = float(x)

    if num.is_integer():  # Check if it has no decimal part
        print("This number is integer")
    else:
        print("This number is float")

if __name__ == "__main__" :
    main()
