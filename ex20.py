# -*- coding: utf-8 -*-

"""
非递归前序遍历
"""

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

def run(root):
    st = [root]
    while len(st) > 0:
        p = st.pop(-1)
        print(p.v)
        if p.r:
            st.append(p.r)
        if p.l:
            st.append(p.l)



root = create(Node(1))
run(root)
