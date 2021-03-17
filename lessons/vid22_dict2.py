classes = {"Ali":["math","science"], #dict icinde list kullandik
           "Veli":["art","bio"],
           "Mehmet":["chem","ESL"]}

#simdi isim girince dersleri veren bi function yazalim

def ders_sorgula():
 while True:
    name = input("write a name:")

    if name not in classes:
        print("try different name")
    else:
        print(f'{name} aldigi dersler sunlardir')
        for i in classes[name]:
            print(i)
        break



ders_sorgula()