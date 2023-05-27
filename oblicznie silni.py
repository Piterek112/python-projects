def obliczaniesilni(n):
    if n == 0:
        return 1
    else:
        return n * obliczaniesilni(n-1)
liczba = int(input("Podaj liczbe do obliczenia slini "))
wynik = obliczaniesilni(liczba)
print(wynik)