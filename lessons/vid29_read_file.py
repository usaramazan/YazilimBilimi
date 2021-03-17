with open("reading_file.txt","r") as dosya:

    print(dosya.read())
    dosya.seek(10) # 10. karakter sonrasini alcak. Yani inlec 10. harfden
    # sonraina locate edecek ama okuma islemi icin yine de read islemini yapmamiz lazim.
    #seek-->her defasinda en bastan sayar
    print(dosya.read())

    dosya.seek(10) # ilk 10 karekter skip edildi ve
    print(dosya.read(5))#sonraki 5 karaketr okundu