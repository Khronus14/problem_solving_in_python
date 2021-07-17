apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

apple_total = apple_one + (apple_two * 2) + (apple_three * 3)

banana_total = banana_one + (banana_two * 2) + (banana_three * 3)

if apple_total > banana_total:
    print('A')
elif apple_total < banana_total:
    print('B')
else:
    print('T')