print("""**************************************
Beden Kitle Indexi Hesaplama Programi
**************************************
""")

boy = float(input("Boyunuzu Giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))
bki = kilo / (boy*boy)
print("\nBeden Kitle Indexiniz :", bki)

if(bki < 18.5):
    print("Zayif")
elif(bki < 25):
    print("Normal")
elif(bki < 30):
    print("Fazla Kilolu")
else:
    print("Obez")