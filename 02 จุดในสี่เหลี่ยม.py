print("Upper left corner coordinate:")
x = int(input("  << x axis: "))
y = int(input("  << y axis: "))
east = int(input("  << Eastern: "))
south = int(input("  << Southern: "))
print("Enter a coordinate:")
find_x = int(input("  << x axis: "))
find_y = int(input("  << y axis: "))
isInX = False
isInY = False

for i in range(x, x + east + 1):
    if find_x == i:
        isInX = True
        break

for i in range(y - south, y + 1):
    if find_y == i:
        isInY = True
        break
    
if isInX and isInY:
    print(f">>> ({find_x:.2f}, {find_y:.2f}) is inside the rectangle.")
else:
    print(f">>> ({find_x:.2f}, {find_y:.2f}) is not inside the rectangle.")
