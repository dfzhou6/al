# -*- coding: utf-8 -*-

"""
最长上升子序列
"""

def run(arr):
    dp = {}
    res = 0
    for i, v in enumerate(arr):
        dp[i] = 1
        j = 0
        while j < i:
            if arr[j] < v:
                dp[i] = max(dp[j] + 1, dp[i])
            j += 1
        res = max(dp[i], res)
    
    return res

print(run([10, 9, 2, 5, 3, 7, 101, 18]))
print(run(range(0, 10)))
        
            
                

            
