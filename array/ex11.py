# -*- coding: utf-8 -*-

"""
爬楼梯
"""

def run(n):
    dp = {}
    i = 1
    while i <= n:
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
        i += 1
    
    return dp[i - 1]

print(run(5))