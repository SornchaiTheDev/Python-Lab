total = 0
round = 0
goal = 0

while True:
    dice1 = int(input())
    dice2 = int(input())
    total = dice1 + dice2
    if dice1 <= 0 or dice2 <= 0 or dice1 > 6 or dice2 > 6:
        print("ERROR")
        continue
    else:
        round += 1

    if round == 1:
        if total == 7 or total == 11:
            print(f"{round} {total} W")
            break
        if total == 2 or total == 3 or total == 12:
            print(f"{round} {total} L")
            break
        goal = total
    else:
        if total == 7:
            print(f"{round} {total} L")
            break
        if total == goal:
            print(f"{round} {total} W")
            break
