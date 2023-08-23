import sys
import os
meno = []
vlastnik = []
prava = []
adresar = []
adresar_vlastnik = []
adresar_prava = []

def kontrola(nazov):
    if nazov == 0:
        print("chyba")
        return

def poradie(nazov):
    for i in range(len(meno)):
        if meno[i] > nazov:
            return i
    return len(meno)

def poradieAdresarov(nazov):
    for i in range(len(adresar)):
        if adresar[i] > nazov:
            return i
    return len(adresar)

def zamena(maska):
    cislo = int(maska)
    switcher = {
        0: '---',
        6: 'rw-',
        5: 'r-x',
        4: 'r--',
        3: '-wx',
        2: '-w-',
        1: '--x',
        7: 'rwx'
    }
    return switcher.get(maska)
def vypis():
    if len(adresar) > 0:
        for i in range(len(adresar)):
            print(adresar[i], end = " ")
            print(adresar_vlastnik[i], end = " ")
            print(zamena(adresar_prava[i]), end = " ")
            print()
    if len(meno) > 0:
        for i in range(len(meno)):
            print(meno[i], end = " ")
            print(vlastnik[i], end = " ")
            print(zamena(prava[i]), end = " ")
            print()
    elif len(adresar) == 0 and len(meno) == 0:
        print("ziaden subor")
def vytvor(nazov):
    cislo = poradie(nazov)
    meno.insert(cislo, nazov)
    try:
        autor = os.getlogin()
    except:
        autor = "root"
    vlastnik.insert(cislo, autor)
    number = 7
    prava.insert(cislo, number)
def vytvorDirectory(nazov):
    cislo = poradieAdresarov(nazov)
    adresar.insert(cislo, nazov)
    try:
        autor = os.getlogin()
    except:
        autor = "root"
    adresar_vlastnik.insert(cislo, autor)
    number = 7
    adresar_prava.insert(cislo, number)
def vymaz(nazov):
    for i in range(len(adresar)):
        if nazov == adresar[i]:
            adresar.pop(i)
            adresar_prava.pop(i)
            adresar_vlastnik.pop(i)
            return
    for i in range(len(meno)):
        if nazov == meno[i]:
            meno.pop(i)
            prava.pop(i)
            vlastnik.pop(i)
            return
    print("chyba")

def precitaj(nazov):
    for i in range(len(meno)):
        if nazov == meno[i]:
            if prava[i] >= 4:
                print("ok")
                return
            else:
                print("chyba prav")
                return

def zapni(nazov):
    for i in range(len(meno)):
        if nazov == meno[i]:
            if (prava[i] % 2 == 1) and (prava[i] != 0):
                print("ok")
                return
            else:
                print("chyba prav")
                return
    
def zmenAdresar(nazov):
    for i in range(len(adresar)):
        if nazov == adresar[i]:
            if (adresar_prava[i] % 2 == 1) and (adresar_prava[i] != 0):
                print("ok")
                return
            else:
                print("chyba prav")
                return
    print("chyba")
def zapis(nazov):
    for i in range(len(meno)):
        if nazov == meno[i]:
            if (prava[i] == 2) or (prava[i] == 3) or (prava[i] == 6) or (prava[i] == 7):
                print("ok")
                return
            else:
                print("chyba prav")
                return
def zmenPrava(nazov, pravo):
    napis = 0
    if pravo == '':
        print("chyba")
        return
    if pravo == 'r--':
        napis = 4
    elif pravo == '-w-':
        napis = 2
    elif pravo == '--x':
        napis = 1
    elif pravo == 'rw-':
        napis = 6
    elif pravo == 'r-x':
        napis = 5
    elif pravo == '-wx':
        napis = 3
    elif pravo == 'rwx':
        napis = 7
    elif pravo == '---':
        napis = 0
    else:
        return
    for i in range(len(meno)):
        if nazov == meno[i]:
            prava[i] = napis
def autor(nazov, autor):
    for i in range(len(meno)):
        if nazov == meno[i]:
            vlastnik[i] = autor
def vstup(val):
    x = val.split()
    if x[0] == 'ls':
        vypis()
    elif x[0] == 'touch':
        if len(x) > 1:
            vytvor(x[1])
        else:
            print("chyba")
            return
    elif x[0] == 'mkdir':
        if len(x) > 1:
            vytvorDirectory(x[1])
        else:
            print("chyba")
            return
    elif x[0] == 'rm':
        if len(x) > 1:
            vymaz(x[1])
        else:
            print("chyba")
            return
    elif x[0] == 'vypis':
        if len(x) > 1:
            precitaj(x[1])
        else:
            print("chyba")
            return
    elif x[0] == 'spusti':
        if len(x) > 1:
            zapni(x[1])
        else:
            print("chyba")
            return
    elif x[0] == 'cd':
        if len(x) > 1:
            zmenAdresar(x[1])
        else:
            print("chyba")
            return
    elif x[0] == 'zapis':
        if len(x) > 1:
            zapis(x[1])
        else:
            print("chyba")
            return
    elif x[0] == 'chmod':
        if len(x) > 2:
            zmenPrava(x[1], x[2])
        else:
            print("chyba")
            return
    elif x[0] == 'chown':
        if len(x) > 1:
            autor(x[2], x[1])
        else:
            print("chyba")
            return
    elif x[0] == 'quit':
        sys.exit()
    else:
        print("chyba")
while(1):
    val = input()
    vstup(val)