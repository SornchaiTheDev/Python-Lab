number = int(input())
sum = 0
while True :
    if number == 0 :
        if sum > 9 :
            number = sum
            sum = 0
            continue
        break
    digit = number % 10
    sum += digit
    number = number // 10


print(sum)