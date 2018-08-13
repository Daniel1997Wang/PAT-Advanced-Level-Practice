#!/usr/bin/env python
# -*- coding: utf-8 -*-

def N_to_Polynomials(N):
    Polynomials = []
    for i in range(int(N[0])):
        temp = []
        temp.append(int(N[2*i+1]))
        temp.append(float(N[2*i+2]))
        Polynomials.append(temp)

    return Polynomials


def main():
    N1 = input("").split(" ")
    N2 = input("").split(" ")


    PolynomialsA = N_to_Polynomials(N1)
    PolynomialsB = N_to_Polynomials(N2)
    Max = PolynomialsA[0][0] + PolynomialsB[0][0]
    Polynomials = []
    for i in range(Max):
        Polynomials.append([(Max-i),0.0])


    for i in range(len(PolynomialsA)):
        for j in range(len(PolynomialsB)):
            K  = PolynomialsA[i][0] + PolynomialsB[j][0]
            sum = round(PolynomialsA[i][1] * PolynomialsB[j][1],2)
            Polynomials[Max-K][1] = Polynomials[Max-K][1] + sum


    Result = []
    for i in range(Max):
        if(Polynomials[i][1] != 0.0):
            Result.append(Polynomials[i])


    print(len(Result), end=" ")
    for i in range(len(Result)):
        if(i != len(Result)-1):
            print(Result[i][0],Result[i][1],end=" ")
        else:
            print(Result[i][0], Result[i][1],end="")



if __name__ == '__main__':
    main()