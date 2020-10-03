# -*- coding: utf-8 -*-

"""
完全二叉树的节点数量
"""

def run(root):
    if root == None:
        return 0
    l_deep = maxDeep(root.left)
    r_deep = maxDeep(root.right)
    if l_deep == r_deep:
        return pow(2, l_deep) + run(root.right)
    else:
        return pow(2, r_deep) + run(root.left)
    
def maxDeep(root):
    n = 0
    while root != None:
        n += 1
        root = root.left
    return n
