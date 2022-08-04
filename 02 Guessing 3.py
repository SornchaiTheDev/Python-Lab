target = 72
count = 0
while True:
    guess = int(input("Enter your guess: "))
    count += 1
    if guess == target:
        print("Congratulations, your guess is correct.")
        break
    if not 0 <= guess <= 100:
        print("Sorry, your guess is out of range.")
    elif guess < target:
        print("Sorry, your guess is too low.")
    else:
        print("Sorry, your guess is too high.")


print(f"Total number of guesses is {count}.")
