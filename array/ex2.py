# -*- coding: utf-8 -*-

"""
最长公共前缀
"""

def run(arr):
    if len(arr) == 0:
        return ""
    
    c_str = ""
    for i, v in enumerate(arr):
        if i == 0:
            c_str = v
        else:
            c_len = len(c_str)
            while c_len > 0:
                if v.find(c_str) != 0:
                    c_len -= 1
                    c_str = c_str[0:c_len]
                else:
                    break
            
            if c_len == 0:
                return ""
    
    return c_str

# arr = ["flue", "fl", "flower", "flow"]
arr = ["flue", "fl", "flower", "flow", "fw"]
rst = run(arr)
print(rst)
            
            
        
