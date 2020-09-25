# -*- coding: utf-8 -*-

"""
两数之和
"""

def run(arr, n):
    dt = {}
    for i, v in enumerate(arr):
        cur = n - v
        if cur in dt:
            return [dt[cur], i]
        else:
            dt[v] = i
        
    return []

arr = [1,2,3,4,5]
ret = run(arr, 10)
print(ret)