import random

def main():
    while True:
        proby = 10
        liczba_wylosowana = random.randint(0, 50)

        while proby > 0:
            proba_gracza = int(input("Podaj liczbę w zakresie od 0 do 50: "))
            if proba_gracza == liczba_wylosowana:
                print(f"Gratulacje! Wylosowana liczba to {liczba_wylosowana}")
                break
            else:
                proby -= 1
                if proby > 0:
                    print(f"Niepoprawna liczba. Pozostało prób: {proby}")
                else:
                    print(f"Przegrałeś. Wylosowana liczba to {liczba_wylosowana}")

        od_nowa = input("Czy chcesz zagrać od nowa? (Tak/Nie): ")
        if od_nowa.lower() != 'tak':
            print("Dziękujemy za grę!")
            break

if __name__ == "__main__":
    main()
