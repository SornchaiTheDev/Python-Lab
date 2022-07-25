import math
number = input()
digits = len(number)
i = 1

if int(number) <= 0 :
    print("ERROR")
else :
    while i <= digits:
        digit = math.floor(int(number)) % 10
        print(digit)
        i += 1
        number = int(number) / 10
