# -*- coding: utf-8 -*-

"""
递归BFS
"""

def run(root, res, lv):
    
    if root == None:
        return res
    
    if len(res) == lv:
        res.append([root.v])
    else:
        res[lv].append(root.v)
    
    res = run(root.l, res, lv + 1)
    res = run(root.r, res, lv + 1)

    return res

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
print(run(root, [], 0))


    
    

        
