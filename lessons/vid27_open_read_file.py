dosya = open("to_do_list.txt","w") # r---read, w----write, a---append(ekle)
#eger biz olusturacagimiz dosyanin yerini de belirlemek istersek dosya adi onune path de eklemek gerekecek
# yani su sekilde "/Users/home/Desktop/to_do_list.txt"
dosya.write("Hi how are you?")
dosya.write("bi oncekini sildi bunu yazdirdi, cunku bu bi w fonksiyonu")

dosya = open("to_do_list.txt","a")
dosya.write("\n Oncekini koruyup bunu eklemis olmali, cunku bu bi 'a' fonksiyonu")