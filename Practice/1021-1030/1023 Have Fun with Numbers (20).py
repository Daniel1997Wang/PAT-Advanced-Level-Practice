#!/usr/bin/env python
# -*- coding: utf-8 -*-


N_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Change_N_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def main():
    #输入
    N = input()
    #操作

    for i in range(len(N)):
        N_count[int(N[i])] += 1

    Change_N = str(2*int(N))
    for i in range(len(N)):
        Change_N_count[int(Change_N[i])] += 1

    Flag = 1
    for i in range(10):
        if(N_count[i] != Change_N_count[i]):
            Flag = 0

    #输出
    if(Flag):
        print("Yes")
    else:
        print("No")

    print(Change_N, end="")



if __name__ == "__main__":
    main()