#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node:
    def __init__(self,root,left,right):
        self.root = root
        self.left = left
        self.right = right


def get_rest(N):
    Number = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    for i in range(20):
        N = N - Number[i]
        if(N <= 0):
            return (N + Number[i])


def Find_root(List):
    N = len(List)
    rest = get_rest(N)
    root = int((N - rest)/2 + 1)+rest
    print(root)
    print(List[:root])
    left = Find_root(List[:root])
    right = Find_root(List[root+1:])
    return Node(root,left,right)


def main():
    List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Find_root(List)











if __name__ == '__main__':
    main()


