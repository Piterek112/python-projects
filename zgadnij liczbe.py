import random
losowa_liczba = random.randint(0, 50)
losowosc = True
while losowosc == True:
    strzal = int(input("Podaj liczbe od 1 do 50 "))
    strzal = int(strzal)
    losowa_liczba = int(losowa_liczba)
    if losowa_liczba == strzal:
        print("Wygrales")
        ponownie = input("Czy chcesz zagrac ponownie? Tak/Nie ")
        if ponownie == 'Tak' or 'tak':
                losowosc = True
        if ponownie == 'Nie' or 'nie':
                losowosc = False
                
    if losowa_liczba > strzal:
        print("Podaj wieksza liczbe liczbe ")
        
    if losowa_liczba < strzal:
        print("Podaj mniejszą liczbe ")
    
    
