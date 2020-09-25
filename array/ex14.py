# -*- coding: utf-8 -*-

"""
三角形最小路径和
"""

import sys

def run(arr):
    dp = {}
    for y, row in arr.items():
        dp[y] = {}
        for x, v in row.items():
            if x == 0 and y == 0:
                dp[y][x] = v
            elif x == 0 and y > 0:
                dp[y][x] = dp[y - 1][x] + v
            elif x == len(row) - 1:
                dp[y][x] = dp[y - 1][x - 1] + v
            else:
                dp[y][x] = min(dp[y - 1][x - 1], dp[y - 1][x]) + v
        if y == len(arr) - 1:
            res = sys.maxsize
            for v in dp[y].values():
                res = min(v, res)
            return res

arr = {
    0: {0: 2},
    1: {0: 3, 1: 4},
    2: {0: 6, 1: 5, 2: 7},
    3: {0: 4, 1: 1, 2: 8, 3: 3}
}
print(run(arr))


        