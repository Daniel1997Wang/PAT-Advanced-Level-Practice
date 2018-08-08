#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    #输入
    N = int(input())
    A_B_C = []
    for i in range(N):
        A_B_C.append(input("").split(" "))

    #操作、输出
    for i in range(N):
        A = int(A_B_C[i][0])
        B = int(A_B_C[i][1])
        C = int(A_B_C[i][2])
        if((A + B) > C):
            if(i != 0):
                print()
            print("Case #",end="")
            print(i+1,end="")
            print(": true",end="")
        else:
            if(i != 0):
                print()
            print("Case #",end="")
            print(i+1,end="")
            print(": false",end="")


if __name__ == "__main__":
    main()