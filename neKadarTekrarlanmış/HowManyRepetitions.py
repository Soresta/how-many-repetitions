import random

"1-9 arası 100 elemanlı bir sayı listesi oluşturun, bu listede her bir sayının kaç kez tekrarlandığını gösterin (bir sözlük kullanın)"
"Create a 100-element list of numbers 1-9, show how many times each number is repeated in this list (use a dictionary)"

liste = []

for i in range(100):
    sayi = random.randint(1, 9)
    liste.append(sayi)
print(liste)

liste2 = []
sözlük = {}

for sayi in liste:
    if sayi in liste2:
        continue
    sayı_hesaplama = liste.count(sayi)
    sözlük.update({sayi: sayı_hesaplama})
    liste2.append(sayi)
print(sorted(sözlük.items()))
