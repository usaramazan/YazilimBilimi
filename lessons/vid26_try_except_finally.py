try:
    dosya = open("yazilimbilimi","r")#eger burda bi sorun
    # cikmazsa, yani bi dosyamiz var ve onu actik. bu kes de onu
    # kapatmamiz gerekiyor. bunun icin de finally kullanacagiz.
except IOError:
    print('dosya bulunamadi')

finally:
    dosya.close() #hata olussa da olusmasa da bu calisir.
    # Boylece bufferda gereksiz yer kaplama engellenmis olur.