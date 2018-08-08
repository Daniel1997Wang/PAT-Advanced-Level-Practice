#!/usr/bin/env python
# -*- coding: utf-8 -*-


def IS_Palindromic_Number(number):
    number = str(number)
    Max_Count = len(number)
    for i in range(Max_Count//2):
        if(number[i] != number[Max_Count-i-1]):
            return False
    return True


def get_Palindromic_Number(number):
    number = str(number)
    Palindromic_Number = ""
    Max_Count = len(number)
    for i in range(Max_Count):
        Palindromic_Number += (number[Max_Count-i-1])
    return int(Palindromic_Number)


def main():
    #输入
    N = input().split(" ")
    number = int(N[0])
    count = int(N[1])

    #操作、输出
    Flag = 1
    for i in range(count):
        if(IS_Palindromic_Number(number)):
            print(number)
            print(i,end="")
            Flag = 0
            break
        else:
            number = number + get_Palindromic_Number(number)
    if(Flag):
        print(number)
        print(count, end="")



if __name__ == "__main__":
    main()