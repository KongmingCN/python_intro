# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:54:07 2019

@author: user
"""

list_input = list(input())
list_result = []

for i in list_input:
    if int(i) == 0:
        break
    else:
        list_result.append(i)

print(list_result)

while len(list_result) > 2:
    list_result = list_result[1:-1]
    print(list_result)