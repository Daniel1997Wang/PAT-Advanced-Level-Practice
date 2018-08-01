#!/usr/bin/env python
# -*- coding: utf-8 -*-

Endlish_number= {0:"zero",  1:"one",
                 2:"two",   3:"three",
                 4:"four",  5:"five",
                 6:"six",   7:"seven",
                 8:"eight", 9:"nine",}

def main():
    number = int(input(""))
    sum = 0
    while(number != 0):
        sum = sum + number % 10
        number = number // 10

    sum_str = str(sum)

    for i in range(len(sum_str)):
        print(Endlish_number[int(sum_str[i])],end="")
        if(i != (len(sum_str) - 1)):
            print(" ",end="")


if __name__ == "__main__":
    main()