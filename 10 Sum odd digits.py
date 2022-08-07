numbers = input("")
total = 0
for number in numbers:
    if int(number) % 2 == 1:
        total += int(number)

if total == 0 :
    print(-1)
else :
    print(total)
