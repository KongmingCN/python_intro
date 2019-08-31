n = 1
mylist = []

while n != 0:
    n = int(input())
    mylist.append(n)
    
    
#print(mylist)
mylist = mylist[:-1]
while len(mylist) > 0:
    print(mylist)
    mylist = mylist[1:-1]
    
# challenge: do not modify mylist