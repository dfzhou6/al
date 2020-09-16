# -*- coding: utf-8 -*-

"""
两个数组的交集
"""

def run(num1, num2):
    dt = {}
    for v in num1:
        if v in dt:
            dt[v] += 1
        else:
            dt[v] = 1

    rst = []
    for v in num2:
        if v in dt and dt[v] > 0:
            dt[v] -= 1
            rst.append(v)

    return rst

num1 = [4, 9, 5]
num2 = [9, 4, 9, 8, 4]

rst = run(num1[:], num2[:])

print(rst)

