#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    msg = input("").split(" ")
    N = int(msg[0])
    n = msg[1]
    Msg = []

    for i in range(N):
        msg = input("").split(" ")
        Msg.append(msg)

    if n == "1":
        res = sorted(Msg,key=lambda Msg :(Msg[0],Msg[1],Msg[2]))
    elif n == "2":
        res = sorted(Msg, key=lambda Msg: (Msg[1], Msg[0],Msg[2]))
    elif n == "3":
        res = sorted(Msg, key=lambda Msg: (Msg[2], Msg[0],Msg[1]))

    for i in range(len(res)):
        if i==(N-1):
            print(res[i][0], res[i][1], res[i][2], end="")
        else:
            print(res[i][0], res[i][1], res[i][2])



if __name__ == '__main__':
    main()