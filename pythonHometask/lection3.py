# последовательности: строки(str), списки(list), кортежи(tuple)
# множества
# словари





def sum_numbers(n):
    summa = 0
    for i in range(1,n+1):
        summa += i
    print(summa)
sum_numbers(6)

def sum_str(*args):
    res = 0
    for i in args:
        res += i
    return res
# print (sum_str('a', 'b', 'c'))
print(sum_str(1, 3, 7))


# modul.py

# import modul_of_lec3
# print(modul_of_lec3.max1(5, 9))
# # from modul_of_lec3 import max1
# # print(max1(5, 9))
# # from modul_of_lec3 import *
# import modul_of_lec3 as m1
# print(m



# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# list_1 = []
# for i in range(1, 2):
#     list_1.append(fib(i))
#     print(list_1)

# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]  # Выбираем первый элемент массива как опорный элемент (пивот)
#         less = [i for i in array[1:] if i <= pivot]  # Создаем список элементов, меньших или равных пивоту
#         greater = [i for i in array[1:] if i > pivot]  # Создаем список элементов, больших пивота
#         return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([7]))
# print_operation_table(lambda x, y: x * y, 3, 3)
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print(' '.join([str(i) for i in range(1, num_columns + 1)]))
        for i in range(2, num_rows + 1):
            row = [str(i)]
            for j in range(2, num_columns + 1):
                row.append(f'{operation(i, j)}')
            print(' '.join(row))
print_operation_table(lambda x, y: x * y, 3, 3)