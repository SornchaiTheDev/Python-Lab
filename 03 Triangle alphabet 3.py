number = int(input("Enter a number: "))

if number <= 0 or number > 26:
    print("Invalid input, program terminates.")
else:

    i1 = 1
    j1 = 1
    text = ""

    while i1 <= number:
        j1 = 1
        while j1 <= i1:
            text += chr(64 + j1)
            j1 += 1

        print(text)
        i1 += 1
        text = ""

    i2 = number - 1
    j2 = 1

    while i2 > 0:
        j2 = 1
        while j2 <= i2:
            text += chr(64 + j2)
            j2 += 1
        
        print(text)
        
        i2 -= 1
        text = ""
