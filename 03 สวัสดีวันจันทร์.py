day = int(input())
hours = int(input())
minutes = int(input())


if day == 1:
    day = "sunday"
elif day == 2:
    day = "monday"
elif day == 3:
    day = "tuesday"
elif day == 4:
    day = "wednesday"
elif day == 5:
    day = "thursday"
elif day == 6:
    day = "friday"
elif day == 7:
    day = "saturday"

if hours in range(4, 12 + 1):
    if hours == 4 and minutes in range(1, 60):
        hours = "morning"
    elif hours == 12 and minutes == 0:
        hours = "morning"
    elif hours != 4 and hours != 12:
        hours = "morning"

if hours in range(12, 18 + 1):
    if hours == 12 and minutes in range(1, 60):
        hours = "afternoon"
    elif hours == 18 and minutes == 0:
        hours = "afternoon"
    elif hours != 12 and hours != 18:
        hours = "afternoon"

if hours in range(18, 22 + 1):
    if hours == 18 and minutes in range(1, 60):
        hours = "evening"
    elif hours == 22 and minutes == 0:
        hours = "evening"
    elif hours != 18 and hours != 22:
        hours = "evening"

if hours in [22, 23, 0, 1, 2, 3, 4]:
    if hours == 4 and minutes == 0:
        hours = "night"
    elif hours == 22 and minutes in range(1, 60):
        hours = "night"
    elif hours != 4 and hours != 22:
        hours = "night"

template = f"good-{hours}-{day}.png"

print(template)
