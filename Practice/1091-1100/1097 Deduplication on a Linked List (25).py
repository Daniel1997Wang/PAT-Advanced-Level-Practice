#! /usr/bin/env python
# -*- coding: utf-8 -*-


def PAT_OUTPUT(list):
    length = len(list)
    list[length-1][2] = "-1"
    list.append(["-1",None,"-1"])
    next = list[0][0]
    for i in range(length):
        if(i != 0):
            print()
        pre = next
        next = list[i+1][0]
        print(pre,list[i][1],next,end="")

def delete_node(link_list):
    saved_link_list = []
    delete_link_list = []
    temp_link_list = []
    for i in range(len(link_list)):
        temp_key = link_list[i][1]
        if(temp_key < 0):
            temp_key = temp_key * -1
        if(temp_key not in temp_link_list):
            temp_link_list.append(temp_key)
            saved_link_list.append(link_list[i])
        else:
            delete_link_list.append(link_list[i])

    return saved_link_list,delete_link_list


def creak_link_list(msg, Pre_address, next):
    pre = next
    link_list = []
    for i in range(len(msg)):
        index = Pre_address.index(pre)
        next = msg[index][2]
        temp = []
        temp.append(pre)
        temp.append(msg[index][1])
        temp.append(next)
        link_list.append(temp)
        pre = next

    return link_list


def INPUT():
    input_msg = input("").split(" ")
    next = input_msg[0]
    N = int(input_msg[1])
    msg = []
    Pre_address = []
    for i in range(N):
        input_msg = input("").split(" ")
        input_msg[1] = int(input_msg[1])
        Pre_address.append(input_msg[0])
        msg.append(input_msg)

    return msg, Pre_address, next


def main():
    #input
    msg, Pre_address, next = INPUT()

    #creak link list
    link_list = creak_link_list(msg,Pre_address,next)

    #delete node
    saved_link_list,delete_link_list = delete_node(link_list)

    #output
    PAT_OUTPUT(saved_link_list)
    print()
    PAT_OUTPUT(delete_link_list)



if __name__ == '__main__':
    main()
    exit(0)