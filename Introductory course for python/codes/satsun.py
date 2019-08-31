days = int(input())
# day of week of the first day
firstDOW = int(input())

dayList = []
# list of day of week of each day
dowList = []
dow = 0
for d in range(days):
    dayList.append(d+1)
    dowList.append(dow)
    # challenge 1: 
    # modify this to a single line of code
    # challenge 2:
    # fix dowList
    # challenge 3:
    # finish the program
    dow = dow + 1
    if dow == 7:
        dow = 0
    
    
print(dayList)
print(dowList)