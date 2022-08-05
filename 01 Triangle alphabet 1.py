number = int(input("Enter a number: "))

if number <= 0 or number > 26:
    print("Invalid input, program terminates.")
else:

    i = 1
    j = 1

    while i <= number:
        j = 1
        while j <= i:
            print(chr(64 + j), end="")
            j += 1
        print()
        i += 1
