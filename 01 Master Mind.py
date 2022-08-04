target = int(input("Enter a target (4-digit integer): "))
save_target = target
guess = int(input("Enter your guess (4-digit integer): "))
save_guess = guess
digits = 0
while True:
    if guess == 0:
        break

    guess_digit = guess % 10

    while True:
        if target == 0:
            break

        target_digit = target % 10

        if guess_digit == target_digit:
            digits += 1

        target = target // 10

    guess = guess // 10
    target = save_target

guess = save_guess
target = save_target
position = 0
while True:
    if guess == 0:
        break

    guess_digit = guess % 10
    target_digit = target % 10

    if target_digit == guess_digit:
        position += 1
        digits -= 1

    target = target // 10
    guess = guess // 10

if digits == 0 and position == 4:
    print("Congratulations, you just mastered my mind!!")
else:
    if digits == 0:
        digits = "no digits"
    elif digits == 1:
        digits = "one digit"
    elif digits == 2:
        digits = "two digits"
    elif digits == 3:
        digits = "three digits"
    else:
        digits = "four digits"

    if position == 0:
        position = "No positions correct"
    elif position == 1:
        position = "One position correct"
    elif position == 2:
        position = "Two position correct"
    elif position == 3:
        position = "Three position correct"

    print(f"{position}, {digits} correct")
