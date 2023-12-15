import sys
import time
def wypisz_dzielniki(liczba):
    dzielniki = []
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            dzielniki.append(i)
    return dzielniki
x= True
print("Kiedy chcesz wyjść, wpisz 'X'")
while x == True:
    liczba_do_sprawdzenia = input("Liczba do sprawdzenia ('X' aby wyjść): ")

    if liczba_do_sprawdzenia.lower() == 'x':
        x = False
    elif not liczba_do_sprawdzenia.isdigit():
        print("Podaj poprawną liczbe")
    else:
        liczba_do_sprawdzenia = liczba_create = int(liczba_do_sprawdzenia)
        if liczba_do_sprawdzenia <= 0:
            print("Podaj liczbe wiekszą niż 0")
            x = True
        else:
            wynik = wypisz_dzielniki(liczba_do_sprawdzenia)
            print(f"Dzielniki liczby {liczba_do_sprawdzenia} to {wynik}")
