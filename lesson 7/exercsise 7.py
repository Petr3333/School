def sum_range(a, b):
    if a > b: # если a < b, то возвращаем значение
        return sum(range(b, a + 1))
    else:
        return sum(range(a,b + 1))


c = int(input())
d = int(input())

print(sum_range(c, d))

