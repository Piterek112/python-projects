
import time
import random
import math
#quiz

punkty = 0
x1 = "Jak nazywa się najważniejsza figura w szachach?"
x2 = "Ile pól znajduje się na standardowej szachownicy?"
x3 = "Jakie figury znajdują się na krańcach szachownicy?"
x4 = "Która figura ma najwięcej możliwośći poruszania się?"
x5 = "Co to jest roszada?"
x6 = "Jak nazywa się sytuacja, w której król jest zagrożony bez możliwości uniknięcia szacha?"
x7 = "Która figura może zbić inne figury skacząc nad nimi na szachownicy?"
x8 = "Co to jest pat?"
x9 = "W którym roku została rozegrana pierwsza udokumentowana partia szachowa?"
x10 = "Jakie są najważniejsze tytuły w hierarchii szachowej?"
print("WItaj w quizie o szachach!")
print("Oto zasady tego quizu:")
print("Quiz składa się z 10 pytań dotyczących szachów.")
print("\n")
print("Każde pytanie jest opisane przez cztery możliwe odpowiedzi, z których tylko jedna jest poprawna.")
print("Twoim zadaniem jest wybrać jedną odpowiedź, która według Ciebie jest poprawna.")
print("Po wybraniu odpowiedzi, otrzymasz natychmiastową informację, czy Twoja odpowiedź jest poprawna.")
print("Przejdź do kolejnego pytania i kontynuuj odpowiedzi w ten sam sposób.")
print("Po zakończeniu quizu, otrzymasz wynik, który wskaże, ile pytań odpowiedziałeś poprawnie.")
print("Jeśli chcesz, możesz ponownie przeglądnąć pytania i odpowiedzi po zakończeniu quizu.")
print("Ciesz się quizem i powodzenia!")
#start
start = True
gotowosc = input("Czy jesteś gotowy? Tak/Nie ")
if gotowosc == 'Tak':
    start = True
else:
    start = False

punkty = 0

while start:
    #pierwsze pytanie
    print("\n")
    print("Pytanie 1\n" + x1)
    print("A) Skoczek")
    print("B) Król")
    print("C) Hetman")
    print("D) Pionek")
    print("\n")    
    odpowiedz1 = input("Poprawna odpowiedź to? ")

    if odpowiedz1.lower() == 'b':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")
        
    time.sleep(0.5)
    #drugie pytanie  
    print("\n")
    print("Pytanie 2\n" + x2)
    print("A) 64")
    print("B) 89")
    print("C) 96")
    print("D) 100")
    print("\n")
    odpowiedz2 = input("Poprawna odpowiedź to? ")

    if odpowiedz2.lower() == 'a':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")
    
    time.sleep(0.5)
    #trzecie pytanie
    print("\n")
    print("Pytanie 3\n" + x3)
    print("A) Konie")
    print("B) Wieże")
    print("C) Królowie")
    print("D) Hetmany")
    print("\n")
    odpowiedz3 = input("Poprawna odpowiedź to? ")

    if odpowiedz3.lower() == 'b':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")

    time.sleep(0.5)
    #czwarte pytanie
    print("\n")
    print("Pytanie 4\n" + x4)
    print("A) Goniec")
    print("B) Pionek")
    print("C) Hetman")
    print("D) Skoczek")
    print("\n")
    odpowiedz4 = input("Poprawna odpowiedź to? ")

    if odpowiedz4.lower() == 'c':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")

    time.sleep(0.5)
    #piate pytanie
    print("\n")
    print("Pytanie 5\n" + x5)
    print("A) Specjalny ruch pionka, który pozwala mu przeskoczyć przeciwnika")
    print("B) Zamiana pionka na inną figurę, gdy dociera do przeciwnej strony szachownicy")
    print("C) Ruch, którym król i wieża zamieniają się miejscami")
    print("D) Ruch, w którym hetman przeskakuje przez przeciwnika")
    print("\n")
    odpowiedz5 = input("Poprawna odpowiedź to? ")

    if odpowiedz5.lower() == 'c':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")

    time.sleep(0.5)
    #szoste pytanie
    print("\n")
    print("Pytanie 6\n" + x6)
    print("A) Szach-Mat")
    print("B) Pat")
    print("C) Roszada")
    print("D) Remis")
    print("\n")
    odpowiedz6 = input("Poprawna odpowiedź to? ")

    if odpowiedz6.lower() == 'a':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")

    time.sleep(0.5)
    #siudme pytanie
    print("\n")
    print("Pytanie 7\n" + x7)
    print("A) Goniec")
    print("B) Hetman")
    print("C) Pion")
    print("D) Skoczek")
    print("\n")
    odpowiedz7 = input("Poprawna odpowiedź to? ")

    if odpowiedz7.lower() == 'd':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")

    time.sleep(0.5)
    #osme pytanie
    print("\n")
    print("Pytanie 8\n" + x8)
    print("A) Sytuacja, w której obie strony nie mogą wygrać")
    print("B)Ruch, którym pionek dociera do przeciwnej strony szachownicy")
    print("C) Ruch, w którym król zamienia się miejscami z wieżą")
    print("D) Sytuacja, w której jeden gracz ma więcej pionków niż drugi")
    print("\n")
    odpowiedz8 = input("Poprawna odpowiedź to? ")

    if odpowiedz8.lower() == 'a':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")

    time.sleep(0.5)
    #dziewiate pytanie
    print("\n")
    print("Pytanie 9\n" + x9)
    print("A) 1475")
    print("B) 1610")
    print("C) 1834")
    print("D) 1874")
    print("\n")
    odpowiedz9 = input("Poprawna odpowiedź to? ")

    if odpowiedz9.lower() == 'a':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")

    time.sleep(0.5)
    #dzisiate pytanie
    print("\n")
    print("Pytanie 10\n" + x10)
    print("A) Mistrz Międzynarodowy (IM), Mistrz FIDE (FM), Mistrz Krajowy (CM)")
    print("B) Arcymistrz (GM), Mistrz Międzynarodowy (IM), Mistrz FIDE (FM)")
    print("C) Arcymistrz (GM), Mistrz Międzynarodowy (IM), Kandydat na Arcymistrza (CM)")
    print("D) Mistrz FIDE (FM), Mistrz Krajowy (CM), Kandydat na Arcymistrza (CM)")
    print("\n")
    odpowiedz10 = input("Poprawna odpowiedź to? ")

    if odpowiedz10.lower() == 'b':
        print("Poprawnie")
        punkty += 1
    else:
        print("Zła odpowiedź, nie dostajesz punktów ")

    time.sleep(0.5)

    




    start = False  # Zmieniamy start na False, aby zakończyć pętlę po trzech pytaniach

print("Twój wynik: {}/10".format(punkty))
                
            
        
    
