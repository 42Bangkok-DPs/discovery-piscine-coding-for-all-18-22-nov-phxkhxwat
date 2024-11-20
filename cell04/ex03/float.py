#!/usr/bin/env python3

x =input("Give me a number: ")
num = float(x)

if num.is_integer():  # Check if it has no decimal part
    print("This number is integer")
else:
    print("This number is float")
