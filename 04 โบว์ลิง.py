round = 10
score = 0
i = 1
while i <= round:
    down = 0
    print(f"Frame # {i}")
    pins = int(input(f"  Number of pins down: "))
    down += pins

    if down == 10:
        score += 10
    else :
        print(f"Frame # {i}")
        pins = int(input(f"  Number of pins down (0-{10 - pins}): "))
        down += pins
        score += down

    i += 1
print(f"Total score is {score}")
