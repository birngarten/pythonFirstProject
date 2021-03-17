sayi = input ("Sayi:")
basamak_sayisi = len(sayi)
sayi = int(sayi)
basamak = 0
toplam = 0

gecici_sayi = sayi

while(gecici_sayi > 0):
    basamak = gecici_sayi % 10
    toplam += basamak ** basamak_sayisi

    gecici_sayi //= 10

if(toplam == sayi):
    print(sayi,"bir amstrong sayidir.")
else:
    print(sayi, " bir amstrong sayi degildir.")