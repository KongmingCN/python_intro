year = int(input())

# all:[ ...may be a leap year... ]
# ->  [ (divisible by 4)..may be.. ,
#        (not divisible by 4)..not leap year.]

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')

# if year divisible by 4 => ???(A)
# otherwise => not leap
# (A) if year divisible by 100 => ???(B)
# otherwise => leap
# (B) if year divisible by 400 => leap
# otherwise => not leap
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, 'is a leap year')
        else:
            print(year, 'is not a leap year')
    else:
        print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')
    
# Challenge: rewrite above program with if-elif-else
    
    