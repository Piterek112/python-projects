import json

# Lista zadan
lista_zadan = []

# Funkcja do zapisu zadań do pliku
def zapisz_zadania_do_pliku(nazwa_pliku):
    with open(nazwa_pliku, "w") as plik:
        json.dump(lista_zadan, plik)

# Funkcja do odczytu zadań z pliku
def odczytaj_zadania_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, "r") as plik:
        zadania = json.load(plik)
        lista_zadan.extend(zadania)

# Główna pętla programu
while True:
    print("===== Zarządzanie Zadaniami =====")
    print("1. Wyświetl zadania")
    print("2. Dodaj zadanie")
    print("3. Oznacz zadanie jako wykonane")
    print("4. Usuń zadanie")
    print("5. Zapisz zadania do pliku")
    print("6. Odczytaj zadania z pliku")
    print("7. Wyjście")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        print("===== Lista Zadań =====")
        if lista_zadan:
            for i, zadanie in enumerate(lista_zadan, start=1):
                wykonane = "✓" if zadanie["wykonane"] else " "
                print(f"{i}. [{wykonane}] {zadanie['opis']}")
        else:
            print("Lista zadań jest pusta.")
        print("=========================")

    elif wybor == "2":
        opis = input("Podaj opis zadania: ")
        zadanie = {"opis": opis, "wykonane": False}
        lista_zadan.append(zadanie)
        print("Zadanie zostało dodane.")

    elif wybor == "3":
        nr_zadania = int(input("Podaj numer zadania do oznaczenia jako wykonane: "))
        if nr_zadania >= 1 and nr_zadania <= len(lista_zadan):
            zadanie = lista_zadan[nr_zadania - 1]
            zadanie["wykonane"] = True
            print("Zadanie zostało oznaczone jako wykonane.")
        else:
            print("Nieprawidłowy numer zadania.")

    elif wybor == "4":
        nr_zadania = int(input("Podaj numer zadania do usunięcia: "))
        if nr_zadania >= 1 and nr_zadania <= len(lista_zadan):
            zadanie = lista_zadan.pop(nr_zadania - 1)
            print(f"Zadanie '{zadanie['opis']}' zostało usunięte.")
        else:
            print("Nieprawidłowy numer zadania.")

    elif wybor == "5":
        nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
        zapisz_zadania_do_pliku(nazwa_pliku)
        print("Zadania zostały zapisane.")

    elif wybor == "6":
        nazwa_pliku = input("Podaj nazwę pliku do odczytu: ")
