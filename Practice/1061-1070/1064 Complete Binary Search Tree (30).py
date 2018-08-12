#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    '''二叉搜索树节点的定义'''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:

    '''二叉搜索树操作'''
    def add(self,root,val):
        """二叉树插入操作"""
        if root == None:
            root = Node(val)
        elif val < root.val:
            root.left = self.add(root.left, val)
        elif val > root.val:
            root.right = self.add(root.right, val)
        return root









    def printTree(self, root):

        # 打印二叉搜索树(中序打印，有序数列)
        if root == None:
            return

        self.printTree(root.left)
        print(root.val, end=' ')
        self.printTree(root.right)





def main():
    List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = None
    tree = Tree()
    for val in List:
        root = tree.add(root, val)
    print('中序打印二叉搜索树：', end=' ')
    tree.printTree(root)










if __name__ == '__main__':
    main()


