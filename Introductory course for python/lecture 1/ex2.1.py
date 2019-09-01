# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:43:02 2019

@author: u3567723
"""

n = int(input())

if n % 4 == 0 and n % 400 == 0:
    print(True)
elif n % 4 == 0 and n % 100 != 0:
    print(True)
else:
    print(False)

