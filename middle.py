bowl_1 = int(input())
bowl_2 = int(input())
bowl_3 = int(input())

if (((bowl_1 > bowl_2) and
        (bowl_1 < bowl_3)) or
    ((bowl_1 < bowl_2) and
        (bowl_1 > bowl_3))):
    print(bowl_1)
elif (((bowl_2 > bowl_1) and
        (bowl_2 < bowl_3)) or
    ((bowl_2 < bowl_1) and
        (bowl_2 > bowl_3))):
    print(bowl_2)
else:
    print(bowl_3)