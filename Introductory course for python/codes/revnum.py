# Q1: what to do in a loop?
# => print(n % 10)
# Q2: how to transit to next iteration?
# => n = n // 10 (or n //= 10)
# Q3: when should we keep going?
# 3756 -> 375
# 375 -> 37
# 37 -> 3
# 3 -> 0
# => when n > 0
# optional Q4: how to start?
# => n = int(input())

#Q4
n = int(input())

#Q3 
while n > 0:
    #Q1
    print(n % 10)
    #Q2
    n = n // 10
    
# challange 1: handle input of 0 (output 0)
# challange 2: handle input of negative number 
    

    