a=int(input('вводим наименьшее число'))
b=int(input('вводим наибольшее число'))
sum = 0
for i in range(a, b+1):
    if i%3==0:
        sum+=i
print(sum)