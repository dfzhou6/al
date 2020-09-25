# -*- coding: utf-8 -*-

"""
股票最佳买卖时机
"""

def run(arr):
    if len(arr) < 2:
        return 0
    
    sum = 0
    for i, v in enumerate(arr):
        if i == 0:
            continue
        if v > arr[i - 1]:
            sum += v - arr[i - 1]
    
    return sum

# arr = [1,2,3,4,5]
# arr = [10,2,3,4,2]
# arr = [10,4,4,4,2]
arr = [10,4,5,4,8]
rst = run(arr)
print(rst)

