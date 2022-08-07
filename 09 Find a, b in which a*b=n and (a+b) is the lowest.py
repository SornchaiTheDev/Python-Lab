n = int(input())
i = 1
lowest = 0
while i <= n:
    a = i
    b = n // i
    if i == 1 :
        lowest = a + b
    if a * b == n :
        if a + b < lowest :
            lowest = a + b
    i += 1

print(lowest)
