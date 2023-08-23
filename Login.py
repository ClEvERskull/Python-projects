import sys
import hashlib


def skontrolujKluc(text, kluc):
    if kluc == "" or text == "":
        print("chyba")
        sys.exit()
    kody = text.split(",")
    for i in range(len(kody)):
        if kluc == kody[i]:
            return i
    print("chyba")
    sys.exit()


def zmazKluc(cislo, pozicia):
    with open("hesla.csv", encoding="utf8") as subor:
        text = subor.read().replace('\n', ':')
    slova = text.split(":")
    zmen = slova[pozicia]
    kody = zmen.split(",")
    kody.pop(cislo)
    x = ",".join(kody)
    slova[pozicia] = x
    with open("hesla.csv", "wb") as subor:
        for i in range(30):
            j = i + 1
            subor.write(slova[i].encode('utf8'))
            if (j % 3) == 0 and j != 30:
                subor.write(b"\n")
            elif (j % 3) > 0:
                subor.write(b":")
    print("ok")
    sys.exit()


def skontroluj(meno, heslo, kluc):
    with open('hesla.csv', encoding="utf8") as subor:
        text = subor.read().replace('\n', ':')
    casti = text.split(":")
    i = 0
    while i < 30:
        if meno == casti[i]:
            m = hashlib.sha1()
            m.update(heslo.encode('utf-8'))
            heslo = m.hexdigest()
            if heslo == casti[i + 1]:
                cislo = skontrolujKluc(casti[i + 2], kluc)
                zmazKluc(cislo, i + 2)
            else:
                print("chyba")
                sys.exit()
        else:
            i += 3
    print("chyba")
    sys.exit()


print("meno:")
meno = str(input()) 
print("heslo:")
heslo = str(input())
print("kluc:")
kluc = str(input())

skontroluj(meno, heslo, kluc)
