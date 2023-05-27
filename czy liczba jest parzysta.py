x = True


while x == True:
    liczba = int(input("Podaj liczbe sprawdze czy jest parzysta "))
    if liczba % 2 == 0:
        print("Liczba jest parzysta")
        x = input("Czy chcesz od nowa? Tak / Nie ")
        if x =='Tak':
            x = True
        if x == 'Nie':
            x = False
            print("Do zobaczenia")
            break
    else:
        print("Liczba nie jest parzysta")
        x = input("Czy chcesz od nowa? Tak / Nie ")
        if x =='Tak':
            x = True
        if x == 'Nie':
            x = False
            print("Do zobaczenia")
            break
        
