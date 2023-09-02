import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
        print(f'{self.os} / {self.nim}\n')

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
data = pd.read_csv('diabetes.csv')

print("Rivien maara (count): ", data.shape[0])
print("Keskiarvo (mean): ")
print(data.min())
print("Minimi (min): ")
print(data.min())
print("Maksimi (max): ")
print(data.max())
print("Keskihajonta (std): ")
print(data.std())

columns = data.columns

num_rows = 3
num_cols = 3

fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))
fig.subplots_adjust(hspace=0.5)
fig.suptitle("Histogrammit kaikista sarakkeista", fontsize=16)

for i, column in enumerate(columns):
    row = i // num_cols
    col = i % num_cols
    ax = axes[row, col]
    ax.hist(data[column], bins=20, edgecolor='k', alpha=0.7)
    ax.set_title(f'{column} - Histogrammi')
    ax.set_xlabel(column)
    ax.set_ylabel('Lukumaara')
    ax.grid(True)
    
plt.show()
#teht 7 loppu

#teht 8 alku
correlation_matrix = data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidth=0.5)
plt.title("Korrelaatiolampokartta")
plt.show()
#teht 8 loppu

#teht 9 alku
sorted_data = data.sort_values(by='Age', ascending=False)
age_counts = sorted_data['Age'].value_counts()

diabetes_counts = data['Outcome'].value_counts()

print("Potilaiden lukumaara ian mukaan (suurimmasta pienimpaan): ")
print(age_counts)

print("\nDiabetes tapaukset (1) ja ei-diabetes tapaukset (0): ")
print(diabetes_counts)
#teht 9 loppu

#teht 10 alku
nan_info=data.isna().sum()

print("Sarakkeet ja niiden NaN-arvojen maara: ")
print(nan_info[nan_info > 0])
#teht 10 loppu
