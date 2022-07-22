number = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))

count = 0
if number < 0 or digit < 0 or digit > 9:

    if number < 0:
        print("Invalid number.")

    if digit < 0 or digit > 9:
        print("Invalid digit.")

else:

    for char in str(number):
        if char == str(digit):
            count += 1
    if count == 1 :
        print(f"Digit {digit} occurs {count} time.")
    else :
        print(f"Digit {digit} occurs {count} times.")
