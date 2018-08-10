#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    #input
    Start = input("").split(" ")
    Start[2] = int(Start[2])
    Store_pre = []
    Store_next = []
    for i in range(Start[2]):
        temp = input("").split(" ")
        Store_pre.append(temp[0])
        Store_next.append(temp[2])


    Start1 = Start[0]
    Start2 = Start[1]

    str = []
    for i in range(Start[2]):
        if(Start1 != "-1"):
            index = Store_pre.index(Start1)
            str.append(Store_pre[index])
            Start1 = Store_next[index]


    flag = 0
    for i in range(int(Start[2])):
        if(Start2 != "-1"):
            index = Store_pre.index(Start2)
            if(Store_pre[index] in str):
                print(Store_pre[index],end="")
                flag = 1
                break
            Start2 = Store_next[index]

    if(flag == 0):
        print("-1",end="")



if __name__ == '__main__':
    main()