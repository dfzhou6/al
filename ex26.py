# -*- coding: utf-8 -*-

"""
删除二叉树节点
"""

def run(root, v):
    if root == None:
        return None
    if v < root.v:
        root.l = run(root.l, v)
        return root
    if v > root.v:
        root.r = run(root.r, v)
        return root
    if root.l == None:
        return root.r
    if root.r == None:
        return root.l
    min_root = root.r
    while min_root.l != None:
        min_root = min_root.l
    root.v = min_root.v
    root.r = delete(root.r)
    return root
        

def delete(root):
    if root == None:
        return None
    
    if root.l != None:
        root.l = delete(root.l)
        return root
    
    return root.r

class Node(object):
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def create(root):
    n2 = Node(5)
    root.l = n2
    n3 = Node(15)
    root.r = n3
    n4 = Node(1)
    n2.l = n4
    n5 = Node(8)
    n2.r = n5
    n6 = Node(11)
    n3.l = n6
    n7 = Node(17)
    n3.r = n7
    return root

root = create(Node(10))
root = run(root, 11)


def bfs(root):

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

bfs(root)

        
    
    
