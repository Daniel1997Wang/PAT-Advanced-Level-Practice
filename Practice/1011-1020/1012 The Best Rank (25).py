#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Student_sored(Student):
    for i in range(len(Student)):
        Student[i] = 100 - Student[i]
    Student_S = sorted(Student)
    for i in range(len(Student)):
        index = Student_S.index(Student[i])
        Student[i] = index + 1

    return Student


def main():
    #输入
    N_M = input("").split(" ")
    Student = []
    Student_ID = []
    for i in range(int(N_M[0])):
        Student.append(input("").split(" "))
    for i in range(int(N_M[1])):
        Student_ID.append(input("").split(" "))


    #操作
    #数据类型转换
    Student_N_ID = []
    Student_C = []
    Student_M = []
    Student_E = []
    Student_A_SUM = []
    for i in range(int(N_M[0])):
        Student_N_ID.append(Student[i][0])
        Student_C.append(int(Student[i][1]))
        Student_M.append(int(Student[i][2]))
        Student_E.append(int(Student[i][3]))
        Student_A_SUM.append((Student_C[i]+Student_M[i]+Student_E[i]))

    Student_M_ID = Student_ID


    #先对C Language Program进行排序
    Student_C = Student_sored(Student_C)
    Student_M = Student_sored(Student_M)
    Student_E = Student_sored(Student_E)
    Student_A_SUM = Student_sored(Student_A_SUM)



    #输出
    Student = []
    Value = ["A","C","M","E"]
    for i in range(int(N_M[1])):
        if(Student_M_ID[i][0] in Student_N_ID):
            index = Student_N_ID.index(Student_M_ID[i][0])
            Temp = []
            Temp.append(Student_A_SUM[index])
            Temp.append(Student_C[index])
            Temp.append(Student_M[index])
            Temp.append(Student_E[index])
            Student.append(Temp)
            if(i!=0):
                print()
            print(min(Temp),end="")
            print(" ",end="")
            print(Value[Temp.index(min(Temp))],end="")
        else:
            if(i!=0):
                print()
            print("N/A",end="")



if __name__ == "__main__":
    main()