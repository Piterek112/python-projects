from forex_python.converter import CurrencyRates

konwerter = CurrencyRates()

kwota_wejsciowa = float(input("Podaj kwotę do przeliczenia: "))
print("Pamietaj zeby pisac skrótem i z duzej litery")
waluta_wejsciowa = input("Podaj walutę wejściową: ")
waluta_wyjsciowa = input("Podaj walutę wyjściową: ")

przeliczona_kwota = konwerter.convert(waluta_wejsciowa, waluta_wyjsciowa, kwota_wejsciowa)

print(f"{kwota_wejsciowa} {waluta_wejsciowa} = {przeliczona_kwota} {waluta_wyjsciowa}")
