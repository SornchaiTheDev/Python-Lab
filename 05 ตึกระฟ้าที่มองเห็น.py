max = 0
count = 0
while True :
    height = int(input())
        
    if height == -1 :
        break

    if height > max :
        count += 1
        max = height

print(count)
