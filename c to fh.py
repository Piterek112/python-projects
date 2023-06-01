import time
c_f = True
f_c = True
caly_program = True
while caly_program == True:
    print("1. C na F")
    print("2. F na C")
    start = input("1 czy 2 " )
    if start == '1':
        f_c = True
    elif start == '2':
        c_f = True

    while f_c == True:
        try:
            f_c2 = int(input("Podaj ile stopni C "))
        except ValueError:
            print("To nie liczba ")
            f_c = True
        
        if f_c2 == 0:
            print("32")

        f_2 = (32+ (f_c2 * 1.8))
        time.sleep(0.3)
        print(f"{f_c2} stopni Celsjusza to {f_2} stopnie Fahrenheita")
        time.sleep(0.3)
        print("\n")
        print("Jeśli chcesz ponownie konwertować wpisz Tak ")
        print("Jeśli chcesz wyjść z programu wpisz Q")
        print("Kiedy chcesz zmieńić operacje wpisz poczatek")
        print("\n")
        od_nowa1 = input("Co chcesz zrobić? ")
        if od_nowa1.lower() == 'tak':
            c_f = True
        elif od_nowa1.lower() == 'q':
            f_c = False
            caly_program = False
            print("Do zobaceznia")
            break
        
        elif od_nowa1.lower() == 'poczatek':
            f_c = False
            c_f = False
            caly_program = True

    while c_f == True:
        try:
            c_f1 = int(input("Podaj ile stopni F "))
        except ValueError:
            print("To nie liczba")
            c_f = True
        
        if c_f1 == 0:
            print("32")
        
        f_1 = ((c_f1 - 32) * 5/9)
        f_1 = round(f_1)
        time.sleep(0.3)
        print(f"{c_f1} stopni Fahrenheita to {f_1} stopni Celsiusza")
        time.sleep(0.3)
        print("\n")
        print("Jeśli chcesz ponownie konwertować wpisz Tak ")
        print("Jeśli chcesz wyjść z programu wpisz Q")
        print("Kiedy chcesz zmieńić operacje wpisz poczatek")
        print("\n")
        od_nowa2 = input("Co chcesz zrobić? ")
        if od_nowa2.lower() == 'tak':
            c_f = True
        elif od_nowa2.lower() == 'q':
            caly_program = False
            print("Do zobaceznia")
        elif od_nowa2.lower() == 'poczatek':
            caly_program = True
        


    


