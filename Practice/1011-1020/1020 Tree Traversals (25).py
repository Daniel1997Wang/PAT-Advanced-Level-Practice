#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def CreatTree(postorder,inorder):
    if len(postorder) == 0:
        return None
    root = postorder[len(postorder)-1]
    index = inorder.index(root)
    left = CreatTree(postorder[:index],inorder[:index+1])
    right = CreatTree(postorder[index:len(postorder)-1],inorder[index+1:])
    return Node(root,left,right)


def level_Traversals(root):
    res, level = [], [root]
    while root and level:
        #currentNode = []
        nextLevel = []
        for node in level:
            #currentNode.append(node.data)
            res.append(node.data)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        level = nextLevel
    return res



def main():
    N = input("")
    postorder = input("").split()
    inorder = input("").split()
    #postorder = [2,3,1,5,7,6,4]
    #inorder = [1,2,3,4,5,6,7]
    root = CreatTree(postorder,inorder)
    res = level_Traversals(root)

    for i in range(len(res)):
        if(i!=(len(res)-1)):
            print(res[i],end=" ")
        else:
            print(res[i],end="")





if __name__ == '__main__':
    main()