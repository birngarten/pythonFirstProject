"""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
"""
def perfect_num(num):
    sum = 0

    for i in range(1, num):

        if (num % i == 0):
            sum += i

    return sum == num


for i in range(1, 1001):

    if (perfect_num(i)):
        print("Perfect_Num:", i)

