import random
import time

print("""
=======================================
IKI SAYININ CARPIM SONUCUNU BULMA OYUNU!

        bir sayi giriniz
=======================================
""")
random_sayi = random.randint(1,200)

tahmin_hakki = 7

while True:

    a = int(input("Tahmininizi Giriniz:"))


    if(a < random_sayi):
        print("\nDaha buyuk bir sayi giriniz!")
        tahmin_hakki -=1

    elif (a > random_sayi):
        print("\nDaha kucuk bir sayi giriniz!")
        tahmin_hakki -= 1

    else:
        print("\nTEBRIKLER! \nDogru Bildiniz...\nSAYI:",random_sayi)
        break

    if (tahmin_hakki == 0):
        print("Tahmin hakkiniz bitti...")

        print("\nDogru Sayi:",random_sayi)
        break