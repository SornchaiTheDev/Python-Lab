import math
x = float(input())

if math.ceil(x) == math.floor(x):
    print(f"{int(x)} is an integer.")
else:
    print(f"{x} is not an integer.")
