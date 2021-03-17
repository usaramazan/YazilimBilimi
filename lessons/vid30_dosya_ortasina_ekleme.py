#Bu list seklindeki bi format uzerinde bi ekleme yapmak
list =[1,2,3,4,5] #simdi birinci index bisey ekliyelim, mesela 34
list.insert(1,34)
print(list)

#simdi de bi list degil de bi dosyanin ortasina ekleme yapalim

with open("reading_file.txt","r+") as dosya:
    data=dosya.readlines() #burda readlines kullanmamizin amaci list
    # seklinde bi return yapmiyor ve boylece biz istedigimiz indexe insert
    # funksiyonu yoluyla ekleme yapabiliriz.
    data.insert(1,"Canan\n")
    dosya.seek(0)
    dosya.writelines(data)

