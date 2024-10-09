from beolvas import *
from random import *
def egyAlap():
    szam1 = beolvasEgesz()
    if szam1 % 2 == 1:
        print("Páratlan")
    else:
        print("Páros")

def egyAlapA():
    szam1 = randint(-10,10)
    if szam1 % 2 == 1:
        print("Páratlan")
    else:
        print("Páros")

def egyAlapB():
    szam1 = randint(-10,10)
    while not(szam1 == 0):
        szam1 = randint(-10,10)
    print(szam1**2)

def egyAlapC():
    szam1 = generalParatlanEgesz()
    print(szam1**2)

def kettoAlap():
    if (szam >= 1 and szam <= 12):
        if szam == 1:
            print("1.hónap - Január")
        elif szam == 2:
            print("2.hónap - Február")
        elif szam == 3:
            print("3.hónap - Március")
        elif szam == 4:
            print("4.hónap - Április")
        elif szam == 5:
            print("5.hónap - Május")
        elif szam == 6:
            print("6.hónap - Június")
        elif szam == 7:
            print("7.hónap - Július")
        elif szam == 8:
            print("8.hónap - Augusztus")
        elif szam == 9:
            print("9.hónap - Szeptember")
        elif szam == 10:
            print("10.hónap - Október")
        elif szam == 11:
            print("11.hónap - November")
        elif szam == 12:
            print("12.hónap - December")
    else:
        print("Nincs " + str(szam) + ". hónap!")

def kettoAlapA():
    szam = randint(-5,15)
    if (szam >= 1 and szam <= 12):
        if szam == 1:
            print("1.hónap - Január")
        elif szam == 2:
            print("2.hónap - Február")
        elif szam == 3:
            print("3.hónap - Március")
        elif szam == 4:
            print("4.hónap - Április")
        elif szam == 5:
            print("5.hónap - Május")
        elif szam == 6:
            print("6.hónap - Június")
        elif szam == 7:
            print("7.hónap - Július")
        elif szam == 8:
            print("8.hónap - Augusztus")
        elif szam == 9:
            print("9.hónap - Szeptember")
        elif szam == 10:
            print("10.hónap - Október")
        elif szam == 11:
            print("11.hónap - November")
        elif szam == 12:
            print("12.hónap - December")
    else:
        print("Nincs " + str(szam) + ". hónap!")

def kettoAlapB():
    