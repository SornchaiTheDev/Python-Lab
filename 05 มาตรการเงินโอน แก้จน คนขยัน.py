age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
total = 0
if 15 <= age <= 60 and (income < 80000 and income > 0) :
    if 1 <= income < 30000 :
        total += income * 0.2
    elif 30000 < income < 80000 :
        total += 30000 * 0.2
        total -= (income - 30000) * 0.12
    print(f"Your negative income tax is {total:.2f} Baht.")
elif age < 15 or age > 60 :
    print("Invalid age.")
else :
    print("Invalid income.")