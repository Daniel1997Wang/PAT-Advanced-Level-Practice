#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    #输入
    Floor = input("").split(" ")
    #操作
    total_time = 0
    Floor[0] = '0'
    pre_time = int(Floor[0])
    for i in range(1,len(Floor)):
        now_time = int(Floor[i])
        temp = now_time - pre_time
        pre_time = now_time
        if(temp > 0):
            total_time = total_time + temp * 6
        else:
            total_time = total_time - temp * 4
        total_time = total_time + 5

    #输出
    print(total_time,end="")


if __name__ == "__main__":
    main()