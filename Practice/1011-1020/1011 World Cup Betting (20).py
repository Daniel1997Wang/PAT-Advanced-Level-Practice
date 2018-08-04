#!/usr/bin/env python
# -*- coding: utf-8 -*-

Result = ["W","T","L"]

def max_score(str_list):
    int_list = [0,0,0]
    for i in range(3):
        temp = str_list[i].split(".")
        temp_number = (int(temp[0]) * 10 + int(temp[1])) / 10
        int_list[i] = temp_number

    max_score = max(int_list)
    index = int_list.index(max_score)
    return round(max_score,1),index

def main():
    #输入
    First_Game = input().split(" ")
    Second_Game = input().split(" ")
    Third_Game = input().split(" ")

    #操作

    First_Game_max,First_Game_index = max_score(First_Game)
    Second_Game_max,Second_Game_index = max_score(Second_Game)
    Third_Game_max,Third_Game_index = max_score(Third_Game)

    max_value = round(First_Game_max * Second_Game_max * Third_Game_max,3)
    maximum_profit = (max_value * 0.65 - 1) * 2

    #输出
    print(Result[First_Game_index],end="")
    print(" ",end="")
    print(Result[Second_Game_index],end="")
    print(" ",end="")
    print(Result[Third_Game_index],end="")
    print(" ",end="")
    print(round(maximum_profit,2),end="")


if __name__ == "__main__":
    main()