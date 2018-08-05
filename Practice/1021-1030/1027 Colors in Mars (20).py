#!/usr/bin/env python
# -*- coding: utf-8 -*-

Thirteen = {0:"0",1:"1",2:"2",3:"3",4:"4",
           5:"5",6:"6",7:"7",8:"8",9:"9",
           10: "A", 11: "B", 12: "C",}


def Earth_To_Mars(number):
    H = number // 13
    L = number % 13
    return Thirteen[H] + Thirteen[L]



def main():
    #输入
    Input_Color = input().split(" ")

    #操作
    Red = int(Input_Color[0])
    Green = int(Input_Color[1])
    Blue = int(Input_Color[2])


    Red = Earth_To_Mars(Red)
    Green = Earth_To_Mars(Green)
    Blue = Earth_To_Mars(Blue)


    #输出
    print("#",end="")
    print(Red, end="")
    print(Green, end="")
    print(Blue, end="")


if __name__ == "__main__":
    main()