height = int(input())
width = int(input())

if width <= 0 or height <= 0:
    print("Invalid input, program terminates.")
else:
    i = 1
    while i <= height:

        if i % 2 == 1:
            print('* ' * width, end='')
        else:
            print(' *' * width, end='')

        print()
        i += 1
