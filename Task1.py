#Найдите сумму цифр трехзначного числа.\
n = int(input("Введите трехзначное число "))
sum = 0
while n > 0:
    sum = sum + n % 10
    n = n // 10
else :
    print(sum)
    