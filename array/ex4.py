# -*- coding: utf-8 -*-

"""
旋转数组
"""

def run(arr, k):
    def func(arr):
        l = len(arr)
        for i in range(l/2):
            tmp = arr[i]
            arr[i] = arr[l-1-i]
            arr[l-1-i] = tmp
        return arr
    
    func(arr)
    arr1 = func(arr[0:k])
    arr2 = func(arr[k:])
    return arr1 + arr2

arr = [1,2,3,4,5,6,7]
k = 2
ret = run(arr, k)
print(ret)