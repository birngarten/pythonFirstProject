def tambolenleribulma(sayi):
    tam_bolenler = []

    for i in range(2,sayi):

        if(sayi % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:

    sayi = input("Sayi:")

    if (sayi == "q"):
        print("Program sonlandiriliyor...")
        break
    else:
        sayi = int(sayi)
        print("tam bolenler:", tambolenleribulma(sayi))