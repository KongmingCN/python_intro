myStr = input()

myStr = myStr * 2

n = 0
while len(myStr) > 0:
    print('_'*n + myStr)
    myStr = myStr[1:-1]
    n += 1