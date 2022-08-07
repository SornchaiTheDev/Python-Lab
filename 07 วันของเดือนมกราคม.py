x = int(input())
n = int(input())
if x <= 0 or x > 7 or n <= 0 or n > 31:
    print("ERROR")
else:
    Day = (n - x) % 7
    if Day == 0:
        print("Sunday")
    elif Day == 1:
        print("Monday")
    elif Day == 2:
        print("Tuesday")
    elif Day == 3:
        print("Wednesday")
    elif Day == 4:
        print("Thursday")
    elif Day == 5:
        print("Friday")
    elif Day == 6:
        print("Saturday")
