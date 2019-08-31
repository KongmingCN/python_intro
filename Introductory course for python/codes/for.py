n = int(input())
prev2 = 0
prev1 = 1
for i in range(n):
    if i == 0:
        print(prev2)
    elif i == 1:
        print(prev1)
    else:
        fib = prev1 + prev2
        print(fib)
        prev2 = prev1
        prev1 = fib