# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:21:17 2019

@author: u3567723
"""

n = int(input())

h = n // 60 ** 2
m = (n // 60) % 60
s = n % 60

print(str(h)+"h",m,"m",s,"s")