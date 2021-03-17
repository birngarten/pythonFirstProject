print("""********************************
Kullanici Girisi
******************************
""")

sys_kullanici_adi = "levent"
sys_parola = "12345"

kullanici_adi = input("Kullanici Adi:")
parola = input("Parola:")

if(kullanici_adi == sys_kullanici_adi and sys_parola != parola):
    print("Parola Hatali!")
elif(kullanici_adi != sys_kullanici_adi and sys_parola == parola):
    print("Kullanici Adi Hatali!")
elif(kullanici_adi != sys_kullanici_adi and sys_parola != parola):
    print("Kullanici Adi ve Parola Hatali!")
else:
    print("Sisteme basari ile giris yapildi")

