# -*- coding: utf-8 -*-

"""
反转字符串
"""

def run(arr):
    l = len(arr)
    n = l/2 - 1
    i = 0
    while i <= n:
        t = arr[i]
        arr[i] = arr[l - 1 - i]
        arr[l - 1 - i] = t
        i += 1
    return arr

arr = ["h", "e", "l", "l", "o"]
print(run(arr))
