# -*- coding: utf-8 -*-

"""
二叉树查找(递归)
"""

def run(root, v):
    if root == None:
        return -1
    if v > root.v:
        return run(root.r, v)
    elif v < root.v:
        return run(root.l, v)
    else:
        return v

class Node(object):
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def create(root):
    n2 = Node(25)
    root.l = n2
    n3 = Node(75)
    root.r = n3
    n4 = Node(20)
    n2.l = n4
    n5 = Node(30)
    n2.r = n5
    n6 = Node(70)
    n3.l = n6
    n7 = Node(80)
    n3.r = n7
    return root

root = create(Node(50))
print(run(root, 10))


