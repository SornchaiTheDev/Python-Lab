number = int(input("Enter a number: "))
if number < 0 :
    print("Invalid input, program terminates.")
else :
    i = 0
    ans = 1
    while i <= number:
        if i > 1 :
            ans *= i
        howto = ""

        j = i
        if i == 0 :
            howto = "1"
        else :
            while j > 0 : 
                howto += str(j)
                if j > 1 :
                    howto += " x "
                    
                j -= 1
                

        print(f"{i}! = {howto} = {ans}")
        i += 1

    
   

    