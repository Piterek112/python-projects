import math
import time

x = False
y = False

co = input("Chcesz potęgować czy pierwiastkować? ")
if co.lower() in ['potęgować', 'potegowac']:
    x = True
if co.lower() in ['pierwiastkować', 'pierwiastkowac']:
    y = True

while x:
    liczba = float(input("Podaj liczbę do potęgowania: "))
    do_ktorej = int(input("Do której potęgi podnieść tę liczbę? "))
    koniec1 = liczba ** do_ktorej
    koniec_potegowania = str(koniec1)
    print(koniec_potegowania)
    pytanie1 = input("Czy chcesz rozpocząć od nowa? Tak/Nie ")
    if pytanie1.lower() != 'tak':
        x = False
        time.sleep(0.5)
        print("Dziękuję")
        break

while y:
    liczba2 = float(input("Podaj liczbę do pierwiastkowania: "))
    pierwiastek = int(input("Jaki pierwiastek? "))
    pierwiastek_koniec = math.pow(liczba2, 1 / pierwiastek)
    print(pierwiastek_koniec)
    pytanie2 = input("Czy chcesz rozpocząć od nowa? Tak/Nie ")
    if pytanie2.lower() != 'tak':
        y = False
        time.sleep(0.5)
        print("Dziękuję")
        break
