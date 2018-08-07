#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    #输入
    Polynomials_A = input("").split(" ")
    Polynomials_B = input("").split(" ")

    #Polynomials_A = ['2', '1', '2.4', '0', '3.2']
    #Polynomials_B = ['2', '2', '1.5', '1', '0.5']

    #初始化多项式的存储结构
    PolynomialsA = []
    for i in range(int(Polynomials_A[0])):
        PolynomialsA.append([0,0])
    PolynomialsB = []
    for i in range(int(Polynomials_B[0])):
        PolynomialsB.append([0, 0])

    Polynomials = []
    for i in range(int(Polynomials_A[0]) + int(Polynomials_B[0])):
        Polynomials.append([0, 0])

    #操作

    #数据类型转换
    j = 0
    for i in range(1,len(Polynomials_A)):
        if(i % 2):
            PolynomialsA[j][0] = int(Polynomials_A[i])
        else:
            PolynomialsA[j][1] = float(Polynomials_A[i])
            j += 1

    j = 0
    for i in range(1,len(Polynomials_B)):
        if(i % 2):
            PolynomialsB[j][0] = int(Polynomials_B[i])
        else:
            PolynomialsB[j][1] = float(Polynomials_B[i])
            j += 1


    #多项式相加运算
    i = 0
    j = 0
    k = 0
    count_zero = 0
    while((i < int(Polynomials_A[0])) and (j < int(Polynomials_B[0]))):
        if(PolynomialsA[i][0] > PolynomialsB[j][0]):
            Polynomials[k][0] = PolynomialsA[i][0]
            Polynomials[k][1] = PolynomialsA[i][1]
            k += 1
            i += 1
        if(PolynomialsA[i][0] < PolynomialsB[j][0]):
            Polynomials[k][0] = PolynomialsB[j][0]
            Polynomials[k][1] = PolynomialsB[j][1]
            k += 1
            j += 1
        else:
            if(PolynomialsA[i][1] + PolynomialsB[j][1] != 0):
                Polynomials[k][0] = PolynomialsA[i][0]
                Polynomials[k][1] = PolynomialsA[i][1] + PolynomialsB[j][1]
            else:
                count_zero += 1
            k += 1
            i += 1
            j += 1

    while(i < int(Polynomials_A[0])):
        Polynomials[k][0] = PolynomialsA[i][0]
        Polynomials[k][1] = PolynomialsA[i][1]
        k += 1
        i += 1

    while(j < int(Polynomials_B[0])):
        Polynomials[k][0] = PolynomialsB[j][0]
        Polynomials[k][1] = PolynomialsB[j][1]
        k += 1
        j += 1

    #输出
    print(k-count_zero,end="")
    for i in range(k-count_zero):
        for j in range(2):
            print(" ", end="")
            print(Polynomials[i][j],end="")


if __name__ == "__main__":
    main()