# print(5)
# print(5, 6, 9)

# n = 5
# print (n)

# n = "dsfwfew"
# print(n)

# n = 5
# print (type(n))

# Найдите сумму цифр трехзначного числа n.

# Результат сохраните в перменную res.

# Пример:



# n = 123 -> res = 6 (1 + 2 + 3)

# n = 100 -> res = 1 (1 + 0 + 0)
# n = input("Введите трехзначное число: ")
# n = int(n)

# d1 = n % 10
# d2 = n % 100 // 10
# d3 = n // 100
# res = d1 + d2 + d3
# print(res)


# задача 2

n = 123456
i = n // 1000
d1 = i % 10
d2 = i % 100 // 10
d3 = i // 100
res1 = d1 + d2 + d3

j = n % 1000
c1 = j % 10
c2 = j % 100 // 10
c3 = j // 100
res2 = c1 + c2 + c3

flag = True
if res1 == res2:
    print('yes')
    flag = False
else:
    print('no')


