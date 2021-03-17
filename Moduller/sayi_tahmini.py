import random
import time
print("""**************************************

      ---  SAYI TAHMIN OYUNU  ---
 
 1 ile 40 arasinda sayiyi tahmin edin.
 
 *************************************
""")


rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7
while True:

    tahmin = int(input("Tahmininiz:"))

    if(tahmin < rastgele_sayi):
        print("Bilgiler Sorgulaniyor...")
        time.sleep(1)

        print("Daha buyuk bir sayi soyleyin...")

        tahmin_hakki -=1

    elif(tahmin > rastgele_sayi):
        print("Bilgiler Sorgulaniyor....")
        time.sleep(1)

        print("Daha kucuk bir sayi soyleyin...")

        tahmin_hakki -= 1

    else:
        print("Bilgiler Sorgulaniyor...")
        time.sleep(1)

        print("\nTEBRIKLER!\nBildiniz...\nSayimiz:", rastgele_sayi)
        break

    if ( tahmin_hakki == 0):
        print("\nTahmin hakkiniz bitti")

        print("\nDogru sayi:", rastgele_sayi)
        break