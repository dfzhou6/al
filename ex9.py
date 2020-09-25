# -*- coding: utf-8 -*-

"""
合并2个有序链表
"""

from ex8 import create_lk, print_lk

def run(lk1, lk2):
    lk = lk1
    tmp = lk
    tmp1 = lk1.next
    tmp2 = lk2.next

    while tmp1 != None and tmp2 != None:
        if tmp1.value >= tmp2.value:
            tmp.next = tmp2
            tmp = tmp2
            tmp2 = tmp2.next
        else:
            tmp.next = tmp1
            tmp = tmp1
            tmp1 = tmp1.next

    if tmp1 != None:
        tmp.next = tmp1
    if tmp2 != None:
        tmp.next = tmp2
    
    return lk

lk1 = create_lk()
lk2 = create_lk()
lk3 = run(lk1, lk2)
print_lk(lk3)


