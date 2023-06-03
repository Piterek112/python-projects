x = True
while x == True:
    liczba_uzytkownika = float(input("Podaj liczbe: "))
    try:
        do_ktorej = int(input("Podaj do której potegi: "))
        x = False
    except ValueError:
        print("Wpisałeś liczbe zmiennoprzecinkową, Spróbuj ponownie")


        
ostateczny_wynik = (liczba_uzytkownika ** do_ktorej)
print(f"Ostateczny wynik to: {ostateczny_wynik}")
    

