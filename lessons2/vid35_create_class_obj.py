class Dusman:
    kalan_can = 3 #kendi olusturdugum instance
    def saldir(self): #self kelimesi kendi olusturdugun instance i tanimlar
        print('Hucuuuum')
        self.kalan_can -=1 #her seferinde 1 azalsin dedim
    def hayatta_mi(self):
        if self.kalan_can<=0:
            print('oldu')
        else:
            print(str(self.kalan_can)+' canim kaldi')



obj1 = Dusman()
obj2 = Dusman()

obj1.saldir()
obj1.saldir()
obj1.saldir()
obj1.hayatta_mi() # obj1 e hem 'saldir' hem de 'hayatta_mi' funksiyonlarinin anlami yuklendi
                # boylece 3 saldi sonunda canlari sifirladi. Ama obj1 ile 3 saldiri yapip
                #obj2 ile hayatta_mi funksiyonunu kullansaydik 'kalan_can'=3 olcakdi
                #yani kime ne anlam yuklediysen o calisir