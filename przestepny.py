x = input("Podaj rok ")

def is_leap_year(year):
    year = int(year)  # Konwersja ciągu znaków na liczbę całkowitą
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'Rok {year} jest przestępny')
            else:
                print(f'Rok {year} nie jest przestępny')
        else:
            print(f'Rok {year} jest przestępny')
    else:
        print(f'Rok {year} jest nieprzestępny')

is_leap_year(x)
