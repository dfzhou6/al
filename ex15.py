# -*- coding: utf-8 -*-

"""
最小路径和
"""

def run(arr):
    dp = {}
    for y, row in arr.items():
        dp[y] = {}
        for x, v in row.items():
            # y, x - 1
            # y - 1, x
            if y == 0 and x == 0:
                dp[y][x] = v
            elif y == 0 and x > 0:
                dp[y][x] = dp[y][x - 1] + v
            elif x == 0 and y > 0:
                dp[y][x] = dp[y - 1][x] + v
            else:
                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1]) + v

    return dp[y][x]

arr = {
    0: {0: 1, 1: 3, 2: 1},
    1: {0: 1, 1: 5, 2: 1},
    2: {0: 4, 1: 2, 2: 1},
}
print(run(arr))

