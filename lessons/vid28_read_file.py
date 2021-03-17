dosya = open("reading_file.txt","r")
print(dosya.read())#dosya icindeki herseyi okur

print(dosya.readline())#dosya acik olduktan sonra en bastaki satiri okur.
# bunu for loop gibi bisey icine koyarsak istedigimiz yere kadar yazdirma isini de yapabiliriz

print(dosya.readlines())# bu list return eder, ve biz istedigimiz line yazdirmak istersek
# su sekilde yapabiliriz
liste = dosya.readlines()
print(liste[1])

#yukaridaki dosya onceden create edildigi icin okuyabildi
#ya o isimde bi dosya yoksa, bu durumda exception hatasi verecek.
#bundan dolayi bu tur codelari try-exception block icinde yapmak daha iyi
try:
    file = open("reading2.txt","r") #normalde bu sekilde bi file onceden create edilmedi
    # "r" islemi tanimlandigi icin except blocku calisacak. normalde "w" or "a" islemi
    # tanimlanmis olsaydi dosya olmasa bile create edielcekti.
    file.read()
except IOError: #FileNotFoundError da yazilabilir
    print("bu isimde bi file yok")