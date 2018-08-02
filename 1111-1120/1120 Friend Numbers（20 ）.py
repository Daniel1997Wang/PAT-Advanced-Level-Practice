#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_number(value):
    sum = 0
    while(value != 0):
        sum = sum + value % 10
        value = value // 10
    return sum


def main():
    #输入
    N = int(input(""))
    Number = input().split(" ")

    #操作
    for i in range(N):
        temp = int(Number[i])
        Number[i] = sum_number(temp)


    Number = sorted(Number)

    Friend_ID = []

    for i in range(len(Number)):
        if(Number[i] not in Friend_ID):
            Friend_ID.append(Number[i])

    #输出
    print(len(Friend_ID))
    for i in range(len(Friend_ID)):
        print(Friend_ID[i],end="")
        if(i != (len(Friend_ID)-1)):
            print(" ",end="")



if __name__ == "__main__":
    main()