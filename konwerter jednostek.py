def przelicz(liczba, jednostka_wejsciowa, jednostka_wyjsciowa):
    # Słownik przeliczników dla różnych jednostek
    przeliczniki = {
        "metry": 1,                # Przelicznik dla metrów
        "centymetry": 0.01,        # Przelicznik dla centymetrów
        "kilometry": 1000,         # Przelicznik dla kilometrów
        "mile": 1609.34,           # Przelicznik dla mil
        "milimetry": 0.001,        # Przelicznik dla milimetrów
        "jardy": 0.9144,           # Przelicznik dla jardów
        "stopy": 0.3048,           # Przelicznik dla stóp
        "cale": 0.0254,            # Przelicznik dla cali
        # Dodaj inne jednostki i ich przeliczniki
    }

    if jednostka_wejsciowa not in przeliczniki or jednostka_wyjsciowa not in przeliczniki:
        return None

    wynik = liczba * (przeliczniki[jednostka_wejsciowa] / przeliczniki[jednostka_wyjsciowa])
    return wynik

def konwerter():
    print("Konwerter jednostek")

    liczba_uzytkownika = float(input("Podaj liczbę: "))  # Wprowadzenie liczby przez użytkownika
    jednostki_wejsciowe = input("Podaj jednostki wejściowe (oddzielone przecinkami): ").split(",")  # Wprowadzenie jednostek wejściowych przez użytkownika
    jednostki_wyjsciowe = input("Podaj jednostki wyjściowe (oddzielone przecinkami): ").split(",")  # Wprowadzenie jednostek wyjściowych przez użytkownika

    for jednostka_wejsciowa in jednostki_wejsciowe:
        for jednostka_wyjsciowa in jednostki_wyjsciowe:
            wynik = przelicz(liczba_uzytkownika, jednostka_wejsciowa.strip(), jednostka_wyjsciowa.strip())  # Wywołanie funkcji przelicz dla danej pary jednostek
            if wynik is not None:
                print(f"{liczba_uzytkownika} {jednostka_wejsciowa.strip()} = {wynik} {jednostka_wyjsciowa.strip()}")  # Wyświetlenie wyniku przeliczenia
            else:
                print("Podano nieobsługiwane jednostki!")  # Wyświetlenie komunikatu o nieobsługiwanych jednostkach

konwerter()  # Wywołanie funkcji konwerter
