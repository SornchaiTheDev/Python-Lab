day = input()
n = int(input())
if day != "Sunday" and day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" or n <= 0 or n > 31:
    print("ERROR")
else:
    if day == "Sunday":
        day = 0
    elif day == "Monday":
        day = 1
    elif day == "Tuesday":
        day = 2
    elif day == "Wednesday":
        day = 3
    elif day == "Thursday":
        day = 4
    elif day == "Friday":
        day = 5
    elif day == "Saturday":
        day = 6
        
    print(day)

    Day = (n - day) % 7
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
