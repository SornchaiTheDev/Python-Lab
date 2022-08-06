target = int(input("Enter a target (4-digit integer): "))
save_target = target
guess = int(input("Enter your guess (4-digit integer): "))
save_guess = guess
digits = 0
target_count = 0
position = 0


while True:
    if target == 0:
        break
    target_digit = target % 10

    guess_count = 0
    while True:
        guess_digit = guess % 10

        if guess == 0:
            break

        if guess_count == target_count and guess_digit == target_digit:
            position += 1
            break

        if guess_digit == target_digit:
            digits += 1

        guess = guess // 10
        guess_count += 1

    target = target // 10
    target_count += 1
    guess = save_guess



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
        position = "Two positions correct"
    elif position == 3:
        position = "Three positions correct"

    print(f"{position}, {digits} correct")
