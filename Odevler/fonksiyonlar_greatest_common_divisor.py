"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""
def gcd(num1,num2):

    i = 1
    ebob = 1

    while (i <= num1 and i <= num2):
        if (  not (num1 % i) and not (num2 % i )):
            ebob = i
        i += 1

    return  ebob

num1 = int(input("num1:"))
num2 = int(input("num2:"))

print("gcd:",gcd(num1,num2))



