sekil = input("Sekil seciniz! ")

if(sekil == "Dortgen"):
    d1 = int(input("1. Kenari Giriniz:"))
    d2 = int(input("2. Kenari Giriniz:"))
    d3 = int(input("3. Kenari Giriniz:"))
    d4 = int(input("4. Kenari Giriniz:"))
    if(d1<=0 or d2<=0 or d3<=0 or d4<=0):
        print("Negatif veya Sifir Deger Girilmez")
    elif (d1==d2==d3==d4):
        print("Bu bir Kare'dir!")
    elif(d1==d3 and d2==d4):
        print("Bu bir Dikdortgen'dir!")
    else:
        print("Dortgen")

elif(sekil == "Ucgen"):
    u1 = int(input("1.Kenari Giriniz:"))
    u2 = int(input("2.Kenari Giriniz:"))
    u3 = int(input("3.Kenari Giriniz:"))
    if(u1<=0 or u2<=0 or u3<=0):
        print("Negatif veya Sifir Deger Girilmez")
    elif(u1==u2==u3):
        print("Eskenar Ucgen!")
    elif(u1==u2 or u1==u3 or u2==u3):
        print("Ikizkenar Ucgen!")
    elif(u1 != u2 !=u3):
        print("Cesitkenar Ucgen")
    else:
        print("Ucgen belirtmiyor")
else:
    print("Dogru Sekil Giriniz!")

