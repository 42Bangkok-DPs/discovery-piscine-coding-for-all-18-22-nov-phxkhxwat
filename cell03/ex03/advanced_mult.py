#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    input_value = sys.argv[1]

    if input_value == "yolo" :
        print("none")
        sys.exit
           
else :
    row = 0
    while row <= 10 :
        colume = 1 
        print("Table de",row,":",end = " ")
        while colume <= 10 :
            print(colume*row , end = " ")
            colume += 1
        print()
        row += 1
