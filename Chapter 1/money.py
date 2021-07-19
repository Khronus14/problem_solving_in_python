total_paint = int(input())

per_bottlecap = int(input())

price = int(input())

badge = total_paint // per_bottlecap

leftover_paint = total_paint % per_bottlecap

print((badge * price) + leftover_paint)