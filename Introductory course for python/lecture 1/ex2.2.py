# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:57:30 2019

@author: u3567723
"""

n = int(input())

while n > 0:
    digit = n % 10
    n = n // 10
    print(digit)