print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")

choose = input("Enter your choice: ").upper()
menu = ""
price = 0

if choose != "B" and choose != "C" and choose != "P":
    print("Invalid main menu choice.")
else:

    if choose == "B":
        print("---<< Burger Sub Menu >>---")
        print("    <R>egular Burger")
        print("    <C>heese Burger")
        print("    <D>ouble Cheese Burger")
        subchoice = input("Enter your choice: ").upper()

        if subchoice == "R":
            menu = "Regular Burger"
            price = 60
        elif subchoice == "C":
            menu = "Cheese Burger"
            price = 75
        elif subchoice == "D":
            menu = "Double Cheese Burger"
            price = 90
        else:
            print("Invalid sub menu choice.")


    if choose == "C":
        print("---<< Chicken Sub Menu >>---")
        print("    <F>ried Chicken")
        print("    <G>rilled Chicken")
        print("    <C>hef's Chicken")
        subchoice = input("Enter your choice: ").upper()
        if subchoice == "F":
            menu = "Fried Chicken"
            price = 120
        elif subchoice == "G":
            menu = "Grilled Chicken"
            price = 150
        elif subchoice == "C":
            menu = "Chef's Chicken"
            price = 180
        else:
            print("Invalid sub menu choice.")

    if choose == "P":
        print("---<< Pasta Sub Menu >>---")
        print("    <S>paghetti de Italiano")
        print("    <L>asagna Supreme")
        print("    <M>acaroni Special")
        subchoice = input("Enter your choice: ").upper()
        if subchoice == "S":
            menu = "Spaghetti de Italiano"
            price = 90
        elif subchoice == "L":
            menu = "Lasagna Supreme"
            price = 120
        elif subchoice == "M":
            menu = "Macaroni Special"
            price = 100
        else:
            print("Invalid sub menu choice.")

if menu != "" and price != 0:
  print(f"Your {menu} is {price} Baht.")
