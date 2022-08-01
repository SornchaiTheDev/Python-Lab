number = int(input())
i = 1

if number <= 0:
    print("ERROR")
else:
    while True:
        if number == 0:
            break
        digit = number % 10
        print(digit)
        i += 1
        number = number // 10
