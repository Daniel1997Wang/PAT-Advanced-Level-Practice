#!/usr/bin/env python
# -*- coding: utf-8 -*-
H = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047]

def find_root(List):
    length = len(List)
    for i in range(len(H)):
        if(length < H[i]):
            h = i
            break

    rest = length - H[h - 1]
    if(rest < pow(2,h-2)):
        right = 0
    elif(rest >= pow(2,h-2)):
        right = rest - pow(2,h-2)

    index = length - 1 - H[h-2] - right
    return List[index]


def find_all_root(list):
    # 找根节点
    root = find_root(list)
    print("root:", root)
    index = list.index(root)

    # 找左节点
    temp_left = list[0:index]
    root = find_root(temp_left)
    print("root:", root)

    # 找右节点
    temp_right = list[index + 1:len(list)]
    root = find_root(temp_right)
    print("root:", root)



def main():
    List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    find_all_root(List)









if __name__ == '__main__':
    main()


