while True:
    number = int(input("Enter a number: "))
    count = 0
    if number == 0:
        print("End of program, goodbye.")
        break

    if number <= 1:
        print("Invalid input, try again.")
        continue

    i = 1
    while i <= number:
        if number % i == 0:
            count += 1
        i += 1

    if count == 2:
        print(f"{number} is a prime number.")

    else:
        print(f"{number} is not a prime number.")
