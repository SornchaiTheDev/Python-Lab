import math

while True :
    print("<<Point a>>")
    xA = int(input("Enter x coordinate: "))
    yA = int(input("Enter y coordinate: "))
    print("<<Point b>>")
    xB = int(input("Enter x coordinate: "))
    yB = int(input("Enter y coordinate: "))

    if xA == 0 and yA == 0 and xB == 0 and yB == 0 :
        print("Goodbye")
        break

    Euclidean = math.sqrt((xA - xB) ** 2 + (yA - yB) ** 2)
    horizontal = xA - xB
    vertical = yA - yB
    directionX = ""
    directionY = ""

    print(f"Distance between ({xA}, {yA}) and ({xB}, {yB}):")
    print(f"Euclidean distance is {Euclidean:.2f}.")
    print(f"Horizontal distance is {abs(horizontal)}.")
    print(f"Vertical distance is {abs(vertical)}.")

    if horizontal < 0 :
        directionX = "east"
    elif horizontal > 0 :
        directionX = "west"
    
    if vertical < 0 :
        directionY = "north"
    elif vertical > 0 :
        directionY = "south"
    
    if horizontal == 0 and vertical == 0:
        print("We are going nowhere.")
        continue

    if directionX != "" and directionY != "" :
        print(f"We are going {directionY}-{directionX}.")
    elif directionX == "":
        print(f"We are going {directionY}.")
    elif directionY == "" :
        print(f"We are going {directionX}.")
   
    
   
    