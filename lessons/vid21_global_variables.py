a=10

def fonction():
    global a
    a = 3 # a'nin global degeri 10 idi ama localde global keyword ile onu 3'e donusturduk
    print(a)

fonction()
print(a)