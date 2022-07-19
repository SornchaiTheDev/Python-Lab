type = input("Enter your buffet choice: ")
isWednesday = False
discount = 1
price = 0
if type != "Korean" and type != "Japanese" :
    print(f"Sorry, there is no {type} buffet.")

else :
    if type == "Korean" :
        price = 1500
    elif type == "Japanese" :
        price = 1000
    condition = input("Is today Wednesday (yes/no)? ")
    if condition == "yes" :
        isWednesday = True
    else :
        isWednesday = False
    
    if isWednesday :
        discount = 0.85

    print(f"Your payment is {(price * discount):.2f} Baht.")