listeler = [2,3,4]

for i in range(1,10): # birde 10 a kadar yazdirmak istiyoruz ama 2,3,4 varsa yazmasin
    if i in listeler:
        continue
    print(i)
