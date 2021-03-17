#kullanici ismi ve parolo knotrol yazilsin

username = input('username: ')
password = input('password: ')

name = "ramazan"
sifre = '12345'

if name==username and sifre==password:
    print('giris yapildi')
else:
    print("username or password is wrong")