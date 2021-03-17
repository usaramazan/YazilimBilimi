sozluk = {"ad":"Ramazan","soyad":"aksit","yas":23}

for i in sozluk:
    print(i) # bu sekilde sadece key leri yazdirdi, value yazdirilmadi


for i in sozluk.items():
    print(i) #bu sekilde key  ile beraber value larida yazdirdi.

    #yukaridan donen sey tuple seklinde oldu
    #ve tuple uzerinden de normal string seklinde yazdirali

for i in sozluk.items():
    print(i[0]+" "+i[1])

# diger bi yol
for i, j in sozluk.items():
    print(i + " "+j)