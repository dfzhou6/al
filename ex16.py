# -*- coding: utf-8 -*-

"""
打家劫舍
"""

import sys

def run(arr):
    dp = {}
    res = -sys.maxsize - 1
    for i, v in enumerate(arr):
        if i == 0:
            dp[i] = v
        elif i == 1:
            dp[i] = max(dp[i - 1], v)
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + v)
        res = max(res, dp[i])
    return res

arr = [2, 7, 9, 3, 1]
print(run(arr))
        
    
