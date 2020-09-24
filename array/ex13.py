# -*- coding: utf-8 -*-

"""
最长上升子序列
"""

def run(arr):
    dp = {}

    for i, v in enumerate(arr):
        if i == 0:
            dp[i] = [v]
            max_v = 1
            continue

        j = 0
        for vv in dp[i - 1]:
            if v > vv:
                j += 1
            else:
                break
        if j + 1 == len(dp[i - 1]) and vv > v:
            dp[i] = dp[i - 1][:-1]
            dp[i].append(v)
        elif j + 1 > len(dp[i - 1]):
            dp[i] = dp[i - 1][:]
            dp[i].append(v)
        else:
            dp[i] = dp[i - 1]
        
        if len(dp[i]) > max_v:
            max_v = len(dp[i])

        print(dp[i])
    
    return max_v

print(run([10, 9, 2, 5, 3, 7, 101, 18]))
        
            
                

            
