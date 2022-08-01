number = int(input())
i = 1
sum = 0
while True:
    if number == 0:
        break
    digit = number % 10
    sum += digit
    number = number // 10
    i += 1

if  number % 9 == sum % 9:
    print(f"Yes {sum}")
else:
    print(f"No {sum % 9}")
