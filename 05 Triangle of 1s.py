height = int(input())
i = 1
while i <= height:
    if i == 1:
        print(f"{1:>11}")
    elif i == 2:
        print(f"{1:>9}   {1:1}")
    elif i == 3:
        print(f"{1:>7}   {1:>5}")
    elif i == 4:
        print(f"{1:>5}   {1:>9}")
    elif i == 5:
        print(f"{1:>3}   {1:>13}")
    elif i == 6:
        print(f"{1:>1}   {1:>17}")

    i += 1

# [ ] หา pattern  ต่อ

"""

          1           (space = 8)
        1   1         (space = 6) (between = 3) 
      1       1       (space = 4) (between = 7)
    1           1     (space = 2) (between = 11)
  1               1   (space = 0) (between = 15)
1                   1
"""
