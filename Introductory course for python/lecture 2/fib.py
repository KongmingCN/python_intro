# -*- coding: utf-8 -*-
'''
Loop Version
'''

n = int(input())

prev1 = 0
prev2 = 1

for i in range(n):
    if i == 0:
        print(prev1)
    elif i == 1:
        print(prev2)
    else:
        fib = prev1 + prev2
        print(fib)
        prev1 = prev2
        prev2 = fib


print('------------------------')

#########################################
'''
Recursive Version
'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)
    

    