# -*- coding: utf-8 -*-

"""
二叉树的深度(递归)
"""

def run(root):
    if root == None:
        return 0
    
    l_deep = run(root.left)
    r_deep = run(root.right)

    return max(l_deep, r_deep) + 1


