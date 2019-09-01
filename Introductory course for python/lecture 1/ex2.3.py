# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:07:12 2019

@author: u3567723
"""

n = int(input())

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(n))