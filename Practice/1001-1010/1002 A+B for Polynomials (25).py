#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    #输入
    Polynomials_A = input("").split(" ")
    Polynomials_B = input("").split(" ")

    #初始化多项式的存储结构

    PolynomialsA_coefficients = [0.0] * 1001
    PolynomialsB_coefficients = [0.0] * 1001
    Polynomials_coefficients = [0.0] * 1001

    #操作
    #数据类型转换
    j = 1
    for i in range(int(Polynomials_A[0])):
        index = int(Polynomials_A[j])
        PolynomialsA_coefficients[index] = round(float(Polynomials_A[j+1]),1)
        j += 2

    j = 1
    for i in range(int(Polynomials_B[0])):
        index = int(Polynomials_B[j])
        PolynomialsB_coefficients[index] = round(float(Polynomials_B[j+1]),1)
        j += 2

    # 多项式相加运算
    count = 0
    for i in range(1001):
        Polynomials_coefficients[i] = PolynomialsA_coefficients[i] + PolynomialsB_coefficients[i]
        if(Polynomials_coefficients[i] != 0.0):
            count += 1

    #输出
    print(count,end="")

    for i in range(1000,-1,-1):
        if (Polynomials_coefficients[i] != 0.0):
            print(" ",end="")
            print(i,end="")
            print(" ", end="")
            print(Polynomials_coefficients[i],end="")


if __name__ == "__main__":
    main()