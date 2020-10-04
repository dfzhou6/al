# -*- coding: utf-8 -*-

"""
滑动窗口的最大值
"""

def run(nums, k):
    n = len(nums)
    if n < k:
        return []
    from sys import maxsize
    max_v = -maxsize - 1
    queue = []
    res = []
    for i, v in enumerate(nums):
        if v >= max_v:
            queue = [i]
            max_v = v
        else:
            if queue[0] == i - k:
                del queue[0]
            while queue and nums[queue[-1]] < v:
                del queue[-1]
            queue.append(i)
            max_v = nums[queue[0]]
        
        if i >= k - 1:
            res.append(max_v)
    return res

nums = [1,3,-1,-3,5,3,6,7]
print(run(nums, 3))

