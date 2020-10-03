# -*- coding: utf-8 -*-

"""
二叉树剪枝
"""

def run(root):
    if root == None:
        return None
    root.left = run(root.left)
    root.right = run(root.right)
    l_check = check(root.left)
    r_check = check(root.right)
    if l_check or r_check or root.val == 1:
        return root
    else:
        return None

def check(root):
    if root == None:
        return False
    l_check = check(root.left)
    r_check = check(root.right)
    return l_check or r_check or root.val == 1
