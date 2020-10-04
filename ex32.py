# -*- coding:utf-8 -*-

"""
无重复字符的最长子串
"""

def run(s):
    if len(s) == 0:
        return 0
    left = 0
    max_len = 0
    dt = {}
    for i, char in enumerate(s):
        if char not in dt:
            dt[char] = i
        else:
            left = dt[char] + 1 if dt[char] + 1 > left else left
            dt[char] = i
        max_len = max(max_len, i - left + 1)
    return max_len

print(run("abcadf"))



