# -*- coding: utf-8 -*-

"""
检查二叉树
"""

import sys

min_v = -sys.maxsize - 1
max_v = sys.maxsize

def run(root, min, max):
    if root == None:
        return True
    if min >= root.v or root.v >= max:
        return False
    return run(root.l, min, root.v) and run(root.r, root.v, max)

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
print(run(root, min_v, max_v))
