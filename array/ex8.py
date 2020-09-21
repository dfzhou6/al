# -*- coding: utf-8 -*-

"""
删除链表倒数第n个节点
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def create_lk():
    lk = Node("start")
    tmp = lk
    for i in range(10):
        node = Node(i)
        tmp.next = node
        tmp = node
    return lk

def print_lk(lk):
    tmp = lk.next
    while tmp != None:
        print(tmp.value)
        tmp = tmp.next

def run(lk, n):
    head = lk.next
    cur = lk
    i = 0

    while head != None:
        i += 1
        if i >= n:
            pre = cur
            cur = cur.next
        head = head.next
    
    cur = pre.next
    pre.next = pre.next.next

    return cur.value

if __name__ == "__main__":
    lk = create_lk()
    print(run(lk, 2))
    print_lk(lk)

