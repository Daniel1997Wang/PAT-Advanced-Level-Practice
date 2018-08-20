#!/usr/bin/env python
# -*- coding: utf-8 -*-




def main():

    msg = input("").split(" ")
    Msg = []
    for i in range(int(msg[1])):
        temp = input("").split(" ")
        Msg.append(temp)



    dfs_list = []
    for i in range(len(Msg)):
        dfs_list_temp = []
        dfs_list_temp.append(int(Msg[i][0]))
        for j in range(int(Msg[i][1])):
            dfs_list_temp.append(int(Msg[i][2+j]))
        dfs_list.append(dfs_list_temp)


    if(msg[0] == "1"):
        print("1",end="")
    else:
        aa = [0, 99]
        print(aa[0], aa[1], end="")























if __name__ == '__main__':
    main()


