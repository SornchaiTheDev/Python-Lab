tv = int(input("How many TVs? "))
dvd = int(input("How many DVD players? "))
audio = int(input("How many Audio Systems? "))
total = (tv * 6000) + (dvd * 1500) + (audio * 3000)
discount = 1
print(f"Total price is {total:.2f} baht.")
if total >= 24000 :
    discount = 0.8
    print(f"You've got a discount of {(total * 0.2):.2f} baht.")
print(f"Your payment is {(total * discount):.2f} baht. Thank you!")

