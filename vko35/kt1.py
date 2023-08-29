import random

print ("Hello world")

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

#teht 6
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