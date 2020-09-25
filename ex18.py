# -*- coding: utf-8 -*-

"""
字符串中第一个唯一字符
"""

def run(words):
    dt = {}
    for i, w in enumerate(words):
        dt[w] = i
    
    for i, w in enumerate(words):
        if w in dt and dt[w] == i:
            return i
        else:
            dt[w] = -1
    
    return -1

print(run("hheelloo"))