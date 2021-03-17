print(*range(7)) #7.indexe kadar sayilari yazdirdik
print(*range(2,9)) #2. indexden 9. indexe kadar yazdirdi
print(*range(2,10,2)) # 2.indexden 10. indexe kadar 2 atlayarak yazdirdik.

#bunlari for loop ile de yapabiliriz
for item in range(5):#indek 0 dan baslayarak 4 e kadar yadirir
    print(item)

for item in range(5,8):# 5,6,7 yazdirir
    print(item)

for item in range(0,8,2):# 2 ser skip counting yapmak istersek
    print(item)