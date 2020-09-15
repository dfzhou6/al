# -*- coding: utf-8 -*-

def run(arr, v):
    """
    原地删除指定数字
    """
    length = len(arr)
    i = 0
    while i < length - 1:
        if v == arr[i]:
            del arr[i]
            length -= 1
        else:
            i += 1
    
    return arr

def run2(arr):
    """
    原地删除有序列表中的重复元素
    """
    length = len(arr)
    
    if length == 1:
        return arr
    
    i = 1
    last = arr[0]
    while i < length - 1:
        if arr[i] == last:
            del arr[i]
            length -= 1
        else:
            i += 1
            last = arr[i]

    return arr
            

arr = [1,2,2,3,4,4,5]
rst = run(arr, 2)
print(rst)

arr2 = [1,2,2,3,4,4,5]
rst = run2(arr2)
print(rst)
