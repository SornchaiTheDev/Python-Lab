"""

Requirement
1. input hours , minutes , shopping , amount
2. waste case only 24 hours
3. 2 hours free charge .
4. 20 bath per hour (3 - 4 hours)
5. 50 bath per hour (5 hours ++ )
6. fraction from hour add to hour
7. buy 300 - 3,000 baht (3 - 4 hours) free
8. buy 3,001 ++ baht free charge

"""
import math
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
buyAmt = int(input("Enter shopping amount: "))
import math
price = 0

if hours < 0 or hours > 20 or minutes < 0 or minutes > 59:
    print("Invalid time.")
else:
    total = hours + math.ceil(minutes / 60)
    if total > 20:
        print("Invalid time.")
    else:
        count = 1
        total -= 2
        while total > 0:
            if count <= 2:
                if buyAmt <= 300:
                    price += 20
                elif buyAmt >= 3001:
                    break

            else:
                price += 50
            count += 1
            total -= 1

        if price == 0:
            print("No charge, thank you.")
        else:
            print(f"Total amount due is {price} Baht, thank you.")
