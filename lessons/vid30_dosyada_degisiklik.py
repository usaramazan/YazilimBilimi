with open("reading_file.txt", "a") as dosya:
     dosya.write("\nbu sona eklendi\n") # write methodu direkt olarak sona yazar

#eger biz hem yazmak hem okumak istersek "r+" kullanmamiz lazim
#dosyanin en basina bi sey yazmak icin bunu kullanmamiz lazim
#cunku once okuyup sonra yazma islemi yapacagiz
with open("reading_file.txt", "r+") as dosya2:
    data = dosya2.read()#once okuduk
    dosya2.seek(0) #simdi en basa gittik
    data = "\nbu basa eklenmis olmali\n" + data
    dosya2.write(data)