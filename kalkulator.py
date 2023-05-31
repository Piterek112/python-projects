import time

print("Witaj w kalkulatorze!")
start = True
print("Wybierz operację:")
print("Dodawanie")
print("Odejmowanie")
print("Mnożenie")
print("Dzielenie")

while start == True:
    x = input("Co chcesz zrobić? ")
    if x.lower() == 'dodawanie':
        dodawanie1 = int(input("Daj mi liczbe "))
        dodawanie2 = int(input("Daj mi drugą liczbe do dodawania "))
        koniec_dodawania = dodawanie1 + dodawanie2
        print(f"Wynik to {koniec_dodawania}")
        time.sleep(0.3)
        start_dodawanie = input("Czy chcesz zacząć od nowa? Tak/Nie ")
        if start_dodawanie.lower() == 'tak':
            start = True
        elif start_dodawanie.lower() == 'nie':
            start = False
            print("Do zobaczenia!")
    elif x.lower() == 'odejmowanie':
        odejmowanie1 = int(input("Podaj liczbe "))
        odejmowanie2 = int(input("Podaj liczbę którą chcesz odjąć "))
        koniec_odejmowania = odejmowanie1 - odejmowanie2
        print(f"Wynik to {koniec_odejmowania}")
        time.sleep(0.3)
        start_odejmowanie = input("Czy chcesz zacząć od nowa? Tak/Nie ")
        if start_odejmowanie.lower() == 'tak':
            start = True
        elif start_odejmowanie.lower() == 'nie':
            start = False
            print("Do zobaczenia")
    elif x.lower() == 'mnożenie':
        mnozenie1 = int(input("Podaj liczbe "))
        mnozenie2 = int(input("Podaj mnożnik "))
        koniec_mnozenia = mnozenie1 * mnozenie2
        print(f"Wynik mnożenia to {koniec_mnozenia}")
        time.sleep(0.3)
        start_mnozenie = input("Czy chcesz zacząć od nowa? Tak/Nie ")
        if start_mnozenie.lower() == 'tak':
            start = True
        elif start_mnozenie.lower() == 'nie':
            start = False
            print("Do zobaczenia")
    
    elif x.lower() == 'dzielenie':
        dzielenie1 = int(input("Podaj liczbe "))
        dzielenie2 = int(input("Podaj dzielnik "))
        koniec_dzielenia = dzielenie1 / dzielenie2
        print(f"Wynik to {koniec_dzielenia}")
        time.sleep(0.3)
        start_dzielenia = input("Czy chcesz zacząć od nowa? Tak/Nie ")
        if start_dzielenia.lower() == 'tak':
            start = True
        elif start_dzielenia.lower() == 'nie':
            start = False
            print("Do zobaczenia")
    else:
        print("Błąd - niepoprawna operacja")
        start = True
