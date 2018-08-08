#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Rank_grade(list):
    for i in range(len(list)):
        list[i] = 100 - int(list[i])
    list_sort = sorted(list)
    for i in range(len(list)):
        index = list_sort.index(list[i])
        list[i] = index + 1
    return list


def main():
    #输入

    Msg = []
    N = int(input(""))
    for i in range(N):
        Msg_N = []
        N_N = int(input(""))
        for j in range(N_N):
            msg = input("").split(" ")
            Msg_N.append(msg)

        Msg.append(Msg_N)


    #对数据预处理
    Msg_ID = []
    Msg_grade = []
    Msg_Tag = []
    Msg_local_grade = []
    for i in range(len(Msg)):
        Msg_temp_grade = []
        for j in range(len(Msg[i])):
            Msg_ID.append(Msg[i][j][0])
            Msg_grade.append(Msg[i][j][1])
            Msg_temp_grade.append(Msg[i][j][1])
            Msg_Tag.append(i+1)

        Msg_local_grade.append(Msg_temp_grade)


    #操作、排序
    Msg_local_rank = []
    for i in range(len(Msg_local_grade)):
        Msg_local_grade[i] = Rank_grade(Msg_local_grade[i])
        for j in range(len(Msg_local_grade[i])):
            Msg_local_rank.append(Msg_local_grade[i][j])


    for i in range(len(Msg_ID)-1):
        for j in range(len(Msg_ID)-i-1):
            if(int(Msg_grade[j]) < int(Msg_grade[j+1])):
                Msg_grade[j],Msg_grade[j+1] = Msg_grade[j+1],Msg_grade[j]
                Msg_ID[j],Msg_ID[j+1] = Msg_ID[j+1],Msg_ID[j]
                Msg_Tag[j],Msg_Tag[j+1] = Msg_Tag[j+1],Msg_Tag[j]
                Msg_local_rank[j],Msg_local_rank[j+1] = Msg_local_rank[j+1],Msg_local_rank[j]


    #输出
    temp = "101"
    temp_rank = 0
    print(len(Msg_ID))
    for i in range(len(Msg_ID)):
        rank = i + 1
        if(i != 0):
            print()
        # 输出ID
        print(Msg_ID[i],end="")
        print(" ",end="")
        #输出总体排名
        if(Msg_grade[i] == temp):
            rank = temp_rank
        print(rank,end="")
        print(" ",end="")
        #输出标签
        print(Msg_Tag[i],end="")
        print(" ",end="")
        # 输出局部排名
        print(Msg_local_rank[i],end="")

        temp = Msg_grade[i]
        temp_rank = rank


if __name__ == "__main__":
    main()