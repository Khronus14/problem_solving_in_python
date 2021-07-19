size = int(input())
cheese = int(input())

if ((size > 2) and
        (cheese > 94)):
    satisfaction = 'absolutely'
elif ((size == 1) or
        (cheese <= 50)):
    satisfaction = 'fairly'
else:
    satisfaction = 'very'

print('C.C. is ' + satisfaction + ' satisfied with her pizza.')
