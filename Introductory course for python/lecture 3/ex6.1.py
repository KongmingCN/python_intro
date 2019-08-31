# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:01:23 2019

@author: user
"""

def myRange(n):
    if n == 0:
        return []
    else:
        return myRange(n-1) + [n-1]

print(myRange(5))


def myRange2(start, end, step):
    pass