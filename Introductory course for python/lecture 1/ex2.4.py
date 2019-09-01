# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:14:55 2019

@author: u3567723
"""

n = int(input())

for i in range(2, n+1):
    if i == 2:
        print(i)
        continue
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)