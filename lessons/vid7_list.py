#ways to add sth to list

list =['ali',34,'Denizli']
list.append("USA")

#other way
print(list + ["Selim"])

#Bi list icinde belirli bi araligi yazdirmak veya degistirmek icin

print(list[:2]) #yani ikinci index e kadar olan kismi yazdir

list[:3]=['a','b','c'] # yani listenin 3. indexine kadar olan kismini yeni verler ile degistir
print(list)

list[:1]=[] # sifirinci index icin bosluk koyduk, boylece birinci index gorunmuyecek

#butun listeyi bosaltabiliriz
list[:]=[]
print(list)