import math
number = input()
digits = len(number)
i = 1
sum = 0
while i <= digits:
    digit = math.floor(int(number) % 10)
    sum += digit
    number = int(number) / 10
    i += 1
if int(number) % 9 == sum % 9 :
    print(f"Yes {sum}")
else:
    print(f"No {sum % 9}")
