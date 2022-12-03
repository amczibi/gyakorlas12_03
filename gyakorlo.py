import random
sorozat = [-3, 5, 11, -2, 4]


def kiiras():
    i = 0
    sep = ";"
    szamok = ""
    while i < len(sorozat)-1:
        szamok += str(sorozat[i]) + sep
        i = i + 1

    print(szamok + str(i))

    veletlen()
    utolso_elem()

def veletlen():
    velszam = int(random.random()*7)+5
    print(velszam)

    szam0 = sorozat[0] + velszam
    print(szam0)



def utolso_elem():
    i = len(sorozat)-1
    print(sorozat[i])


def kiiras2():
    while True:
        beker = int(input("Adjon meg egy hárommal osztható kétjegyű számot! "))
        if (beker // 10 < 10) and (beker // 10 > 0) and (beker % 3 == 0) and (beker%2 != 0):
            sorozat.append(beker)
        else:
            print("Nem megeflelő szám!")


"""def kiiras2():
   
    while True:
        beker = int(input("Adjon meg egy hárommal osztható kétjegyű számot! "))
        if (beker // 10 < 10) and (beker // 10 > 0) and (beker % 3 == 0) and (beker%2 != 0):
            sorozat.append(beker)
        else:
            print("Nem megeflelő szám!")"""

"""
sorozat=[1,2,3,4,5]
def feladat2():
    szam = int(input("3-mal osztható, nem páros, kétjegyű szám"))
    
    while not ((szam >= 10) and (szam <= 99) and (szam%2 ==1) and (szam%3==0)):
        szam = int(input("3-mal osztható, nem páros, kétjegyű szám"))
    print(szam)
    sorozat[len(sorozat)-1] = szam
    """
#egy paraméterében megadott számról eldönti, hogy prímszám-e

def primszam():
    szam = int(input("Adjon meg egy prímszámot!"))
    while not szam % 2 !=0 and szam % 3 != 0 and szam % 5 != 0 and szam % 7 !=0:
        szam = int(input("Adjon meg egy prímszámot!"))

    print("A szám prímszám")

