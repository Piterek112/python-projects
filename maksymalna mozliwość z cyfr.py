from functools import reduce

def obliczaniesilni(n):
    if n == 0:
        return 1
    else:
        return n * obliczaniesilni(n-1)

n = int(input("Podaj liczbę liczb do wprowadzenia: "))

liczby = []
for i in range(n):
    liczba = int(input("Podaj liczbę: "))
    liczby.append(liczba)

wynik = reduce(lambda x, y: x * y, liczby)
wynik = str(wynik)
print("Masz: " + wynik + " Kombinacji")
n = str(n)
print(f"To znaczy: "+ n +"!")
