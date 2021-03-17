

#eger biz num2 yerine kullanici yanlislikla bi string
# gonderse veya 0 koysa hata verir. bu durumda try except kullaniriz.
try:
    num1 = int(input("number1:")) #aldigimiz degerler de try block icinde olmali
    num2 = int(input("number2:"))
    print(num1/num2)

except ZeroDivisionError:
    print('you can not divide by 0')
except ValueError:
    print('dont send string')