a = int(input())
b = int(input())
c = int(input())

isRightTriangle = False


if a <= 0 or b <= 0 or c <= 0:
    pass
else:
    if a > b:
        if a > c:
            angle3 = a
            angle1 = b
            angle2 = c
        else :
            angle3 = c
            angle1 = a
            angle2 = b        
    elif b > c:
        angle3 = b
        angle1 = a
        angle2 = c
    else:
        angle3 = c
        angle1 = a
        angle2 = b
    
    isRightTriangle = (angle1 ** 2) + (angle2 ** 2) - angle3 ** 2 == 0

print(isRightTriangle)
