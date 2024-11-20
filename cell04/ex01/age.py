#!/usr/bin/env python3
def main():
    x = input("Please tell me you age: ")
    age = int(x)

    print("You are currently", age , "years old.")

    for i in range(10,40,10):
        print("In ", i , "years , you'll be " , age+i ,"years old.")

if __name__ == "__main__" :
    main()
