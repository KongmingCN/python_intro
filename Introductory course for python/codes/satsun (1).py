days = int(input())
# day of week of the first day
dow = int(input())

dayList = []

for d in range(days):
    # derive the actural day of week
    dow2 = (d + dow) % 7
    if dow2 == 6 or dow2 == 0:
        dayList.append(d+1)
        
print(dayList)