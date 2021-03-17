vize1 = int(input("1.Vize Notunuzu Giriniz:"))
vize2 = int(input("2.Vize Notunuzu Giriniz:"))
final = int(input("Final Notunuzu Giriniz:"))

note = vize1*0.3 + vize2*0.3 + final*0.4

if(note >= 90):
    print(note ," -> AA")
elif(note >= 85):
    print(note ," -> BA")
elif(note >= 80):
    print(note ," -> BB")
elif(note >= 75):
    print(note ," -> CB")
elif(note >= 70):
    print(note +" -> CC")
elif(note >= 65):
    print(note ," -> DC")
elif(note >= 60):
    print(note ," -> DD")
elif(note >= 55):
    print(note ," -> FD")
else:
    print(note ," -> FF")