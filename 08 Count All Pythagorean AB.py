c = int(input())

i = 1
j = 1
count = 0
while i <= c:
    j = 1
    while j <= i:
        if (i ** 2 + j ** 2) == c ** 2:
            count += 1
        j += 1
    i += 1

print(count)
