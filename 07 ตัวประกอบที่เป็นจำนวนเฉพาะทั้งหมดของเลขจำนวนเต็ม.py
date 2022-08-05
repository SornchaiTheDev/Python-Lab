integer = int(input("Enter positive integer: "))

if integer <= 0:
    print("Invalid number.")
else:
    i = 2
    number = integer
    while i <= number:
        if number % i == 0:
            print(i)
            number = number / i
            i = 2
            continue
        i += 1
