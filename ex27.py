# -*- coding: utf-8 -*-

"""
平衡二叉树
"""

def run(root):
    if root == None:
        return True
    l_b = run(root.left)
    r_b = run(root.right)
    if l_b == False or r_b == False:
        return False

    l_deep = max_deep(root.left)
    r_deep = max_deep(root.right)
    if abs(l_deep - r_deep) > 1:
        return False
    return True

def max_deep(root):
    if root == None:
        return 0
    l_deep = max_deep(root.left)
    r_deep = max_deep(root.right)
    return max(l_deep, r_deep) + 1
