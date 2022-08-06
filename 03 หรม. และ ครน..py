firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

first = firstNumber
second = secondNumber
gcd = 1
if first == second :
    gcd = first
else :
    while True:
        
        mod = first % second
        if mod > 0:
            first = second
            second = mod
        else:
            break
        gcd = mod

lcm = gcd
lcm *= firstNumber // gcd
lcm *= secondNumber // gcd


print(f"  >> gcd({firstNumber}, {secondNumber}) ={gcd:>7d}")
print(f"  >> lcm({firstNumber}, {secondNumber}) ={lcm:>7d}")
