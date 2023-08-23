import sys

def reversing(text):
    return text[::-1]

def count_digits(n):
    n = str(n)
    return len(n)

def make_array(txt):
    n = count_digits(txt)
    x = 0
    y = 0
    z = 0
    number = ''
    for x in range(len(txt)):
        if x == 0:
            z = n - 1
       
        else:
            z = x - 1
        
        if x < (n - 1):
            y = x + 1
        
        else:
            y = 0

        val1 = ord(txt[x])
        val2 = ord(txt[y])
        val3 = ord(txt[z])
        var = val1 * val2
        var = var - val3
        while var > 1112063:
            var = var - 1112063
        while var < 0:
            var = var + 1112063
        number += chr(var)
    
    return number

def sifrovanie(file, key):
    x = 0
    crypted = ''

    #for i in range(len(file)):
    with open(str(sys.argv[file]), encoding="utf8") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            var = ord(c) + ord(key[x])
            if var > 1112063:
                var = var - 1112063
            crypted += chr(var)
            x = x + 1
            if (count_digits(key) >= x):
                x = 0
    return crypted

def desifrovanie(file, key):
    x = 0
    decrypted = ''

    with open(str(sys.argv[file]), encoding="utf8") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            var = ord(c) - ord(key[x])
            if var < 0:
                var = var + 1112063
            decrypted += chr(var)
            x = x + 1
            if (count_digits(key) >= x):
                x = 0
    return decrypted


if len(sys.argv) != 5:
    print('Chyba')
    sys.exit()

heslo_je = 0
x = 2
n = len(sys.argv) - 1
for i in range(len(sys.argv)):
    if sys.argv[i] == '-s':
        x = 0
    elif sys.argv[i] == '-d':
        x = 1
    elif sys.argv[i] == '-p':
        heslo_je = i + 1

key = reversing(sys.argv[heslo_je])
heslo = make_array(key)
if x == 0:
    crypted = sifrovanie(n, heslo)
    print(crypted)
elif x == 1:
    decrypted = desifrovanie(n, heslo)
    print(decrypted)
else:
    print("chyba")
