def myRange(m, n=None, step=1):
    if n == None:
        return _myRange(0, m, step)
    
    return _myRange(m, n, step)
    
def _myRange(start, end, step):
    i = start
    mylist = []
    while i < end:
        mylist.append(i)
        i += step
    
    return mylist

print(myRange(10))
print(myRange(2, 10))
print(myRange(2, 10, 2))









