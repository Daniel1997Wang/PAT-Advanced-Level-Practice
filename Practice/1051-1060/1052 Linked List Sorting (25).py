#！/usr/bin/env python
# -*- coding：utf-8  -*-


def main():
    #input
    input_msg = input("").split(" ")
    N = int(input_msg[0])
    next = input_msg[1]
    #特殊情况
    if(next == "-1"):
        print(0,-1,end="")
        exit(0)

    msg = []
    pre_address = []
    for i in range(N):
        input_msg = input("").split(" ")
        input_msg[1] = int(input_msg[1])
        pre_address.append(input_msg[0])
        msg.append(input_msg)


    #对不是链上的数据进行处理
    i = 0
    pre = next
    Msg = []
    while(next != '-1'):
        temp = []
        index = pre_address.index(pre)
        msg_temp = msg[index][1]
        next = msg[index][2]
        temp.append(pre)
        temp.append(msg_temp)
        temp.append(next)
        pre = next
        i += 1
        Msg.append(temp)


    Msg = sorted(Msg, key=lambda Msg: Msg[1])

    #output
    N = len(Msg)
    next = Msg[0][0]
    print(N,next)
    for i in range(N):
        if(i != 0):
            print()
        pre = next
        print(pre,end="")
        print(" ",end="")
        print(Msg[i][1], end="")
        print(" ", end="")
        if(i < N-1):
            next = Msg[i+1][0]
        else:
            next = -1
        print(next, end="")



if __name__ == '__main__':
    main()
    exit(0)