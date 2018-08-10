#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    #输入
    N = int(input(""))
    Msg = []
    for i in range(N):
        Msg_N = []
        N_N = int(input(""))
        for j in range(N_N):
            msg = input("").split(" ")
            msg[0] = int(msg[0])
            msg[1] = int(msg[1])
            msg.append((i+1))
            Msg_N.append(msg)
        #数据预处理
        Msg_N = sorted(Msg_N,key= lambda Msg_N :(-Msg_N[1],Msg_N[0]))
        Msg.append(Msg_N)


    #操作、排序
    Result = []
    #对local rank进行排序
    for i in range(len(Msg)):
        temp = Msg[i][0][1]
        rank = 1
        for j in range(len(Msg[i])):
            if(Msg[i][j][1] != temp):
               rank = j + 1
            Msg[i][j].append(rank)
            temp = Msg[i][j][1]
            Result.append(Msg[i][j])


    Result = sorted(Result,key = lambda Result: (-Result[1],Result[0]))
    # 对fianl rank进行排序

    temp = Result[0][1]
    rank = 1
    for i in range(len(Result)):
        if(Result[i][1] != temp):
            rank = i + 1

        temp = Result[i][1]
        Result[i][1] = rank


    #输出
    print(len(Result))
    for i in range(len(Result)):
        if(i != 0):
            print()
        print(Result[i][0],end="")  # 输出ID
        print(" ",end="")
        print(Result[i][1], end="") #输出总体排名
        print(" ", end="")
        print(Result[i][2], end="") #输出标签
        print(" ", end="")
        print(Result[i][3],end="")  # 输出局部排名


if __name__ == "__main__":
    main()