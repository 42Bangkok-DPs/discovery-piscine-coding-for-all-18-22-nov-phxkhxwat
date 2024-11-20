#!/usr/bin/env python3

def main():
    print("Enter a number")
    x = int(input())

    for i in range (0,10):
        print(i ,"x",x , "=" ,i*x)

if __name__ == "__main__" :
    main()