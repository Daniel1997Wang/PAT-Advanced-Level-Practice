#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    #输入
    N = int(input(""))
    Number = input().split(" ")
    for i in range(N):
        Number[i] = int(Number[i])

    #操作

    #选择排序的算法
    """
    第一趟从n个元素的数据序列中选出关键字最小/大的元素并放在最前/后位置，
    下一趟从n-1个元素中选出最小/大的元素并放在最前/后位置。
    
    for i in range(len(Number)-1):
        min_index = i
        for j in range(min_index+1,len(Number)):
            if Number[j] < Number[min_index]:
                min_index = j
        Number[i],Number[min_index] = Number[min_index],Number[i]
    """
    Number = sorted(Number)

    A1 = []
    A2 = []

    if(N%2 == 0):
        temp = N//2
        sum_A2 = 0
        print(0,end="")
    else:
        temp = (N+1)//2
        sum_A2 = Number[temp-1]
        print(1,end="")

    print(" ", end="")



    sum_A1 = 0

    for i in range(N//2):
        A1.append(Number[i])
        A2.append(Number[temp+i])
        sum_A1 = sum_A1 + A1[i]
        sum_A2 = sum_A2 + A2[i]



    #输出
    print(sum_A2-sum_A1,end="")


if __name__ == "__main__":
    main()