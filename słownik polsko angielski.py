slownik = {
    "airplane": "samolot",
    "bag": "torba",
    "basketball": "koszykówka",
    "bed": "łóżko",
    "bicycle": "rower",
    "book": "książka",
    "bus": "autobus",
    "car": "samochód",
    "chair": "krzesło",
    "city": "miasto",
    "clock": "zegar",
    "clothes": "ubrania",
    "computer": "komputer",
    "cup": "kubek",
    "dog": "pies",
    "door": "drzwi",
    "drums": "perkusja",
    "eraser": "gumka",
    "flower": "kwiat",
    "football": "piłka nożna",
    "fork": "widelec",
    "friend": "przyjaciel",
    "glasses": "okulary",
    "guitar": "gitara",
    "hat": "kapelusz",
    "house": "dom",
    "key": "klucz",
    "knife": "nóż",
    "map": "mapa",
    "moon": "księżyc",
    "mountain": "góra",
    "movie": "film",
    "music": "muzyka",
    "newspaper": "gazeta",
    "pants": "spodnie",
    "pen": "długopis",
    "pencil": "ołówek",
    "piano": "pianino",
    "plate": "talerz",
    "radio": "radio",
    "reading": "czytanie",
    "river": "rzeka",
    "running": "bieganie",
    "school": "szkoła",
    "shoes": "buty",
    "shirt": "koszula",
    "ship": "statek",
    "shopping": "zakupy",
    "spoon": "łyżka",
    "sun": "słońce",
    "swimming": "pływanie",
    "table": "stół",
    "tablecloth": "obrus",
    "telephone": "telefon",
    "television": "telewizor",
    "tennis": "tenis",
    "tree": "drzewo",
    "umbrella": "parasolka",
    "violin": "skrzypce",
    "watch": "zegarek",
    "window": "okno",
    "writing": "pisanie"
}


def znadz_tlumaczenie(slowo, slownik):
    slowo = slowo.lower()
    if slowo in slownik:
        return slownik[slowo]
    else:
        return "Brak tłumaceznia tego słowa."

def dodaj__tlumaczenie(slowo, tlumaceznie, slownik):
    slowo = slowo.lower()
    slownik[slowo] = tlumaceznie

def usun_tlumaczenie(slowo, slownik):
    slowo = slowo.lower()
    if slowo in slownik:
        del slownik[slowo]
        print("Usunięto tłumaczenie")
    else:
        print("Brak tłumaczenia dla tego słowa.")
    
def wyświetl_slownik(slownik):
    print("Słownik angielsko polski:")
    for slowo, tlumaczenie, in slownik.items():
        print(f"slowo": "{tlumaczenie}")

while True:
    print("\nCo chcesz zrobić?")
    print("1. Znajdź tłumaczenie")
    print("2. Dodaj tłumaczenie")
    print("3. Usuń tłumaczenie")
    print("4. Wyświetl słownik")
    print("5. Wyjdź")

    wybor = input("Twój wybór: ")
    if wybor == "1":
        slowo = input("Podaj słowo do przetłumaczenia: ")
        tlumaczenie = znajdz_tlumaczenie(slowo, slownik)
        print(tlumaczenie)
    elif wybor == "2":
        slowo = input("Podaj słowo w języku angielskim: ")
        tlumaczenie = input("Podaj tłumaczenie słowa: ")
        dodaj_tlumaczenie(slowo, tlumaczenie, slownik)
        print("Dodano tłumaczenie.")
    elif wybor == "3":
        slowo = input("Podaj słowo do usunięcia: ")
        usun_tlumaczenie(slowo, slownik)
    elif wybor == "4":
        wyswietl_slownik(slownik)
    elif wybor == "5":
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")