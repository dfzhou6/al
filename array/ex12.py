# -*- coding: utf-8 -*-

"""
最大子序和
"""

def run(arr):
    dp = {}
    
    for i, v in enumerate(arr):
        if i == 0:
            dp[i] = v
            max_v = v
        elif dp[i - 1] + v > v:
            dp[i] = dp[i - 1] + v
        else:
            dp[i] = v

        if dp[i] > max_v:
            max_v = dp[i]
        
    return max_v

print(run([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


        
    

            

