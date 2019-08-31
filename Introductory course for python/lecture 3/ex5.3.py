# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:29:41 2019

@author: user
"""
d = int(input())
for i in range(d):
    
    n = 10 ** i
    pi = 0
    
    for i in range(n):
        pi += (-1) ** i * 4 / (2 * i + 1)
    
    print(f'|{n}|{pi}|')