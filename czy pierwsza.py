import time  # Importuje moduł time

def czy_pierwsza(liczba):
    if liczba < 2:  # Jeśli liczba jest mniejsza niż 2
        return False  # Zwraca False, ponieważ liczba nie może być liczbą pierwszą
    for i in range(2, int(liczba ** 0.5) + 1):  # Pętla sprawdzająca podzielniki liczby
        if liczba % i == 0:  # Jeśli liczba jest podzielna przez i
            return False  # Zwraca False, ponieważ liczba nie jest liczbą pierwszą
    return True  # Jeśli pętla nie znalazła żadnego podzielnika, zwraca True, czyli liczba jest liczbą pierwszą

def czy_jest_pierwsza(lista_liczb):
    liczby_pierwsze = []  # Tworzy pustą listę na liczby pierwsze
    liczby_zlozone = []  # Tworzy pustą listę na liczby złożone
    
    for liczba in lista_liczb:  # Iteruje po podanej liście liczb
        if czy_pierwsza(liczba):  # Jeśli liczba jest liczbą pierwszą
            liczby_pierwsze.append(liczba)  # Dodaje ją do listy liczb pierwszych
        else:
            liczby_zlozone.append(liczba)  # Dodaje ją do listy liczb złożonych
    
    return liczby_pierwsze, liczby_zlozone  # Zwraca dwie listy: liczby_pierwsze i liczby_zlozone

def wpisz_wynik(liczby_pierwsze, liczby_zlozone):
    print("Liczby pierwsze: ")  # Wypisuje nagłówek dla liczb pierwszych
    for liczba in liczby_pierwsze:  # Iteruje po liście liczb pierwszych
        print(f"Liczba {liczba} jest liczbą pierwszą.")  # Wypisuje informację o liczbie pierwszej
    print("\nLiczby złożone: ")  # Wypisuje nagłówek dla liczb złożonych
    for liczba in liczby_zlozone:  # Iteruje po liście liczb złożonych
        print(f"Liczba {liczba} jest liczbą złożoną.")  # Wypisuje informację o liczbie złożonej
    
def wprowadz_liczby():
    liczby = []  # Tworzy pustą listę na liczby
    
    while True:  # Wykonuje pętlę nieskończoną
        liczba_użytkownika = input("Podaj liczbe(lub 'q' aby zakonczyc wpisywanie liczb) ")  # Pobiera liczbę od użytkownika jako tekst
        
        if liczba_użytkownika.lower() == 'q':  # Jeśli użytkownik wprowadził 'q'
            break  # Przerywa pętlę, kończąc wprowadzanie liczb
        
        try:
            liczba = int(liczba_użytkownika)  # Konwertuje wprowadzoną wartość na liczbę całkowitą
            liczby.append(liczba)  # Dodaje liczbę do listy liczb
        except ValueError:
            print("Nieprawidłowe dane. Wprowadź liczbe ")  # Wyświetla komunikat o nieprawidłowych danych
    
    return liczby  # Zwraca listę wprowadzonych liczb

liczby_użytkownika = wprowadz_liczby()  # Pobiera liczby od użytkownika
liczby_pierwsze, liczby_zlozone = czy_jest_pierwsza(liczby_użytkownika)  # Wywołuje funkcję sprawdzającą, czy liczby są pierwsze
wpisz_wynik(liczby_pierwsze, liczby_zlozone)  # Wypisuje wyniki dla liczb pierwszych i złożonych
