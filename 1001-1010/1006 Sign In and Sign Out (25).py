#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    #输入
    N = int(input(""))
    Input_Msg = []
    for i in range(N):
        msg = input("").split(" ")
        Input_Msg.append(msg)

    #操作
    for i in range(len(Input_Msg)):
        temp = Input_Msg[i][1].split(":")
        value = int(temp[2]) + int(temp[1]) * 60 + int(temp[0]) * 60 * 60
        Input_Msg[i][1] = value

        temp = Input_Msg[i][2].split(":")
        value = int(temp[2]) + int(temp[1]) * 60 + int(temp[0]) * 60 * 60
        Input_Msg[i][2] = value


    min_value = Input_Msg[0][1]
    max_value = Input_Msg[0][1]
    min_index = 0
    max_index = 0
    for i in range(len(Input_Msg)):
        if Input_Msg[i][1] < min_value:
            min_value = Input_Msg[i][1]
            min_index = i
        if Input_Msg[i][2] > max_value:
            max_value = Input_Msg[i][2]
            max_index = i
    #输出
    print(Input_Msg[min_index][0],end="")
    print(" ",end="")
    print(Input_Msg[max_index][0],end="")





if __name__ == "__main__":
    main()