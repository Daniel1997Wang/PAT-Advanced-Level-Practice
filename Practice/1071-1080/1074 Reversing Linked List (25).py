#！ /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    #input
    input_msg = input("").split(" ")
    next_address = input_msg[0]
    N = int(input_msg[1])
    K = int(input_msg[2])
    if(K == 1):
        K = N + 1
    if(N == 0):
        exit(0)
    msg = []
    PRE_address = []
    for i in range(N):
        input_msg = input("").split(" ")
        msg.append(input_msg)
        PRE_address.append(input_msg[0])



    Msg = []
    while(next_address != '-1'):
        temp = []
        pre_address = next_address
        index = PRE_address.index(pre_address)
        next_address = msg[index][2]
        temp.append(pre_address)
        temp.append(msg[index][1])
        temp.append(next_address)
        Msg.append(temp)


    PRINT_MSG = []
    N = len(Msg)
    count = 0
    while(N >= 0):
        N = N - K
        if(N >= 0):
            for j in range(count*K,(count+1)*K):
                index = K - j - 1
                temp = []
                temp.append(Msg[index][0])
                temp.append(Msg[index][1])
                PRINT_MSG.append(temp)
            count += 1


    if(N < 0):
        N = N + K
        for index in range((count*K),(count*K+N)):
            temp = []
            temp.append(Msg[index][0])
            temp.append(Msg[index][1])
            PRINT_MSG.append(temp)

    temp = []
    temp.append("-1")
    temp.append(None)
    PRINT_MSG.append(temp)


    #output
    next_address = PRINT_MSG[0][0]
    for i in range(len(PRINT_MSG)-1):
        if(i != 0):
            print()
        pre_address = next_address
        print(pre_address,end="")
        print(" ",end="")
        print(PRINT_MSG[i][1], end="")
        print(" ", end="")
        next_address = PRINT_MSG[i+1][0]
        print(next_address,end="")



if __name__ == '__main__':
    main()
    exit(0)