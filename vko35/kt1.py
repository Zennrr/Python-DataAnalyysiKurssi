import random


#teht 1 alku
print ("Hello world!")
#teht 1 loppu

#teht 2 alku
c = input("Syota numero c: ")
d = input("Syota toinen numero d: ")

if c > d:
    print ("c on isompi")
elif d > c:
    print ("d on isompi")
else:
    print ("yhtä suuret")
#teht 2 loppu

#teht 3 alku
a = random.randint(0, 100)
b = random.randint(0, 100)

print (f'a: {a}')
print (f'b: {b}')

if a > b:
    print ("a on isompi")
elif b > a:
    print ("b on isompi")
else:
    print ("yhtä suuret")
#teht 3 loppu

#teht 4 alku
e = random.randint(0, 10)
f = random.randint(0, 10)

def summaus():
    summa = e + f
    print (f'lukujen e({e}) ja f({f}) summa on {summa}')

summaus()
#teht 4 loppu

#teht 5 alku
pisteet = 0
piste = 1
print ("Laske kertolaskut:")
for i in range(5):
    g = random.randint(0, 10)
    h = random.randint(0, 10)
    
    tulo = g * h
    
    vastaus = int(input(f'{g} * {h} = '))
    
    if vastaus == tulo:
        print(f'Oikein! {g} x {h} = {tulo}\n')
        pisteet += piste
    elif vastaus != tulo:
        print(f'Vaarin! Oikea vastaus on {tulo}\n')

print(f'Sait {pisteet} oikein!\n')
#teht 5 loppu

#teht 6 alku
class Murtoluku:
    def __init__(self, os, nim):
        self.os = os
        self.nim = nim

    def tulosta(self):
        print(f'{self.os} / {self.nim}')

    def sievenna(self):
        syt = self.syt() #syt = math.gcd(self.os, self.nim)
        self.os //= syt #self.os = self.os / syt
        self.nim //= syt

    def syt(self):
        a = self.os
        b = self.nim

        while b != 0:
            t = b
            b = a % b
            a = t
        return a
        
ml = Murtoluku (2000, 400000)

ml.tulosta()
ml.sievenna()
ml.tulosta()
#teht 6 loppu

#teht 7 alku
