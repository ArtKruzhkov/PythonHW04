# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k
# import random
# size1 = int(input('Enter size:'))
# koef = {}
# for i in range(size1 + 1):
#     koef[i] = random.randint(0, 101)
# print(koef)
# equation = ''
# for i in range(size1, -1, -1):
#     if koef[i] != 0:
#         if koef[i] == 1:
#             if i == 1:
#                 equation = equation + f'x + '
#             elif i == 0:
#                 equation = equation + f'1 '
#             else:
#                 equation = equation + f'x**{i} + '
#         else:
#             if i == 1:
#                 equation = equation + f'{koef[i]}*x + '
#             elif i == 0:
#                 equation = equation + f'{koef[i]} '
#             else:
#                 equation = equation + f'{koef[i]}*x**{i} + '
# print(equation + ' = 0')




# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Сделал что просто вот заданы 2 многочлена, и выдаем сумму их сумму строкой sum (без файлов)
# import random
# size1 = int(input('Enter size:'))
# size2 = int(input('Enter size:'))
# def Create(size):
#     koef = {}
#     for i in range(size + 1):
#         koef[i] = random.randint(0, 101)
#     print(koef)
#     equation = ''
#     for i in range(size, -1, -1):
#         if koef[i] != 0:
#             if koef[i] == 1:
#                 if i == 1:
#                     equation = equation + f'1*x + '
#                 elif i == 0:
#                     equation = equation + f'1 '
#                 else:
#                     equation = equation + f'1*x**{i} + '
#             else:
#                 if i == 1:
#                     equation = equation + f'{koef[i]}*x + '
#                 elif i == 0:
#                     equation = equation + f'{koef[i]} '
#                 else:
#                     equation = equation + f'{koef[i]}*x**{i} + '
#     return equation + '= 0'
# dict1 = Create(size1)
# dict2 = Create(size2)
# print()
# print(f'Polynomial1 = {dict1}')
# print(f'Polynomial2 = {dict2}')

# dict1 = dict1.replace(' ', '')
# dict1 = dict1[:-2].split('+')
# print(f'Elements = {dict1}')

# dict2 = dict2.replace(' ', '')
# dict2 = dict2[:-2].split('+')
# print(f'Elements = {dict2}')

# dicto = dict(enumerate(dict1, 1))                # сложение элементов словарей и вывод их в новую строку sum                                                 # привел списки к словарям чтобы через условие и and получить пары и выявить эл.
# dicto2 = dict(enumerate(dict2, 1))               # привел списки к словарям чтобы через услов. и and получить парные эл. и безпар.                                                # у которых пар нету
# sum = ''
# if(len(dicto)) > (len(dicto2)):
#     for i in dicto.keys():
#         if dicto.get(i) and dicto2.get(i):           
#             sum = sum + f'{dicto[i]} + {dicto2[i]} + '
#         else:
#             sum = sum + f'{dicto[i]} + '
# elif(len(dicto2)) > (len(dicto)):
#     for i in dicto2.keys():
#         if dicto.get(i) and dicto2.get(i):          
#             sum = sum + f'{dicto2[i]} + {dicto[i]} + '
#         else:
#             sum = sum + f'{dicto2[i]} + '
# else:
#     for i in dicto.keys():
#         if dicto.get(i) and dicto2.get(i):           
#             sum = sum + f'{dicto[i]} + {dicto2[i]} + '
# print('Sum for these polynomials =')
# print(sum + '= 0')