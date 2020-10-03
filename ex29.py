# -*- coding: utf-8 -*-

"""
完全二叉树的节点数量(递归)
"""

def run(root):
    if root == None:
        return 0
    l_deep = run(root.l)
    r_deep = run(root.r)
    return l_deep + r_deep + 1
