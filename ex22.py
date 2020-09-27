# -*- coding: utf-8 -*-

"""
非递归BFS
"""

def run(root):

    lv = 0
    res = {}
    if root == None:
        return lv
    res[lv] = [root]
    
    while lv in res:
        for node in res[lv]:
            print(node.v)
            if node.l:
                if lv + 1 not in res:
                    res[lv + 1] = [node.l]
                else:
                    res[lv + 1].append(node.l)
            if node.r:
                if lv + 1 not in res:
                    res[lv + 1] = [node.r]
                else:
                    res[lv + 1].append(node.r)
        lv += 1
    
    return lv
            

class Node(object):
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def create(root):
    n2 = Node(2)
    root.l = n2
    n3 = Node(3)
    root.r = n3
    n4 = Node(4)
    n2.l = n4
    n5 = Node(5)
    n2.r = n5
    n6 = Node(6)
    n3.l = n6
    n7 = Node(7)
    n3.r = n7
    return root

root = create(Node(1))
print(run(root))
