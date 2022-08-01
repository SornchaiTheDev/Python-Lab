height = int(input("Enter height: "))
space = 3
if height > 0:
    i = height * 2 - 2
    while i >= 0:
        if i == height * 2 - 2:
            print(" " * i, end="")
            print(1)
        else:
            print(" " * i, end="")
            print(1, end="")
            print(" " * space, end="")
            print(1)

            space += 4
        i -= 2


"""

          1           (space = 10) (between = 0)
        1   1         (space = 8)  (between = 3) 
      1       1       (space = 6)  (between = 7)
    1           1     (space = 4)  (between = 11)
  1               1   (space = 2)  (between = 15)
1                   1 (space = 0)  (between = 19)
"""
