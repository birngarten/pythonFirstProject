print("""
**********
Eve Giris
**********
""")

userName = "can"
password = "mine"

girisHakki = 3

while True:
    kullaniciAdi = input("Kullanici Adi:")
    parola = input("Parola:")

    if (userName != kullaniciAdi and password==parola):
        print("Kullanici Adi Hatali!")
        girisHakki -= 1

    elif (userName == kullaniciAdi and password != parola):
        print("Parolaniz Hatali!")
        girisHakki -= 1

    elif (userName != kullaniciAdi and password != parola):
        print("Kulanic Adiniz ve Parolaniz Hatali!")
        girisHakki -= 1

    else:
        print("Evinize Hosgeldiniz...")
        break

    if (girisHakki == 0):
        print("Eve basarili giris yapamadiniz! 5 dakika sonra tekrar deneyiniz...")
        break