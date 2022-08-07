numbers = input("")
total = 1
hasEven = False
for number in numbers:
    if int(number) % 2 == 0:
        total *= int(number)
        hasEven = True

if not hasEven:
    print(-1)
else:
    print(total)
