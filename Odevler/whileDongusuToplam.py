summ = 0

while True:

    num = input("Nummer:")
    if(num == "q"):
        break
    num = int(num)

    summ += num

print("Summer :", summ)
