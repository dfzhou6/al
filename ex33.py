# -*- coding:utf-8 -*-

def run(s, p):
    p_len = len(p)
    s_len = len(s)
    if p_len == 0 or s_len == 0 or p_len > s_len:
        return []

    def check(dt_s, dt_p):
        for k, v in dt_p.items():
            if k not in dt_s or v != dt_s[k]:
                return False
        return True

    res = []
    left = 0

    dt_p = {}
    for pp in p:
        dt_p[pp] = dt_p.get(pp, 0) + 1
    
    dt_s = {}
    for ss in s[:p_len]:
        dt_s[ss] = dt_s.get(ss, 0) + 1

    if check(dt_s, dt_p):
        res.append(left)

    left += 1
    while left <= s_len - p_len:
        dt_s[s[left - 1]] -= 1
        dt_s[s[left + p_len - 1]] = dt_s.get(s[left + p_len - 1], 0) + 1
        if check(dt_s, dt_p):
            res.append(left)
        left += 1
        
    return res

print(run("abac", "abc"))

