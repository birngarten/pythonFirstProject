num = int(input("Sayi:"))

i = 1
sum = 0

while(i < num):
    if( num % i ==0):
        sum += i
    i +=1
if(sum == num):
    print(num, " mukemmel bir sayidir.")
else:
    print(num, " mukemmel bir sayi degildir.")

