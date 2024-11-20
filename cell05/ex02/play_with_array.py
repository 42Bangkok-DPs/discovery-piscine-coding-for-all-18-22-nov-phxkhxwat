#!/usr/bin/env python3

def main():
    arr = [2,8,9,48,8,22,-12,2]
    print("Original array: " ,arr)

    new_arr = []

    for i in arr :
        if i > 5 :
            new_arr.append(i+2) 
    print("New array: " ,new_arr)

if __name__ == "__main__" :
    main()

