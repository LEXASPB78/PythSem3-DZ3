# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# number = int(input('Введите размер списка '))
# list = []
# sum = 0
# for i in range(number):
#     list_number = int(input(f'Введите число {i+1} '))
#     list.append(list_number)
#     if i % 2 != 0:
#         sum += list[i]


# print(list)
# print(f'Сумма нечетных чисел равна {sum}')


my_list = [8, 5, 7, 3, 6]
print(sum(my_list[1::2]))