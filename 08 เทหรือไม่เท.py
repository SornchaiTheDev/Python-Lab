import math
minutes = float(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")

if rain == "y" or rain == "Y":
    rain = True
elif rain == "n" or rain == "N":
    rain = False

days = math.floor((minutes / 60 / 24) + 0.5)

print(f">>> {days} days before due.")

if days < 2 :
        print(">>> I will do the assignment.")
elif 2 <= days <= 5 :
    if (temp <= 40 and temp <= 25 or not rain):
        print(">>> I will do the assignment.")
    else :
        print(">>> I will not do the assignment.")
else:
    print(">>> I will not do the assignment.")