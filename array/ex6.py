# -*- coding: utf-8 -*-

"""
加一
"""

def run(arr):
    i = len(arr) - 1
    plus = 0

    if arr[i] + 1 > 9:
        plus = 1
        arr[i] = 0
    else:
        arr[i] += 1
        
    i -= 1
    while i >= 0 and plus == 1:
        if arr[i] + plus > 9:
            arr[i] = 0
            plus = 1
        else:
            arr[i] += plus
            plus = 0
        i -= 1
    
    if plus == 1:
        arr.insert(0, 1)

    return arr

arr = [0]
ret = run(arr)
print(ret)
            


