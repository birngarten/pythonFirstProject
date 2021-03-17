"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
"""
def lcm(num1,num2):
    i = 2
    ekok = 1

    while True:
        if ( num1 % i == 0 and num2 % i == 0):
            ekok *= i

            num1 //= i
            num2 //=i

        elif ( num1 % i == 0 and num2 % i != 0):
            ekok *= i

            num1 //= i

        elif (num1 % i != 0 and num2 % i == 0):
            ekok *= i

            num2 //= i

        else:
            i += 1
        if ( num1 == 1 and num2 == 1):
            break
    return ekok

num1 = int(input("num1:"))
num2 = int(input("num2:"))

print("LCM:", lcm(num1,num2))