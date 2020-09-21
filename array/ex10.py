# -*- coding: utf-8 -*-

"""
判断闭环（双指针和hash解法）
"""

from ex8 import create_lk, create_close_lk, print_lk

def run(lk):
    s1 = lk
    if lk.next == None:
        return False
    s2 = lk.next.next
    
    while s1 != None and s2 != None:
        if s1.value == s2.value:
            return True
        s1 = s1.next
        if s2.next == None:
            return False
        s2 = s2.next.next

    return False

cl = create_close_lk()
print(run(cl))
cl = create_lk()
print(run(cl))
    
