height = input("Podaj wzrost ")
weight = input("Podaj wage ")
height = float(height)
weight = float(weight)
bmi = weight / (height**2)
print(bmi)
if bmi <= 16.0:
    print("Wygłodzenie")
if bmi >= 16.0 and bmi <= 16.9:
    print("Wychudzenie ")
if bmi >=17.0 and bmi <= 18.5:
    print("Niedowaga")
if bmi >= 18.6 and bmi <= 24.9:
    print("Waga prawidłowa")
if bmi >=25.0 and bmi <= 29.9:
    print("Nadwaga")
if bmi >=30.0 and bmi <= 34.9:
    print("Otyłość 1 stopnia")
if bmi >= 35.0 and bmi <= 39.9:
    print("Otyłość 2 stopnia")
if bmi >= 40:
    print("Mega otyłość")
