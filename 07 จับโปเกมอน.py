pokemon_lv = int(input("Enter level pokemon: "))
pokeball_lv = input("Enter level pokeball: ")
distance = int(input("Enter distance: "))

if pokeball_lv != "H" or pokeball_lv != "M" or pokeball_lv != "L" or pokeball_lv != "h" or pokeball_lv != "m" or  pokeball_lv != "l" :
    if pokeball_lv == "H" or pokeball_lv == "h" :
            pokeball_lv = 0.01
    if pokeball_lv == "M" or pokeball_lv == "m" :
            if 0 <= pokemon_lv <= 40 :
                pokeball_lv = 0.03
            elif pokemon_lv <= 60 :
                pokeball_lv = 0.05
            elif pokemon_lv <= 100 :
                pokeball_lv = 0.08
            
    if pokeball_lv == "L" or pokeball_lv == "l" :
            if 0 <= pokemon_lv <= 40 :
                pokeball_lv = 0.05
            elif pokemon_lv <= 60 :
                pokeball_lv = 0.03
            elif pokemon_lv <= 100 :
                pokeball_lv = 0.1
            
        
        
    formular = 100 - (pokemon_lv * distance * pokeball_lv)
    if formular > 100 :
        formular = 100
    elif formular < 0 :
        formular = 0
    print(f"{formular:.2f} percent.")
