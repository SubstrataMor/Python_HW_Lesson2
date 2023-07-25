# Задача 1 сложная необязательная:
# Посчитать сумму цифр любого целого или вещественного числа.
# Через строку решать нельзя.

from decimal import Decimal

summa = int(0)
number = Decimal(str(input('Введите вещественное или целое число: ')))  # преобразуем ввод числа с консоли в тип Decimal
if number%1 >0:
    while number % 1 > 0:       # Если число вещественное, то избавляемся от дробной части
        number *= 10
print(number)
number = int(number)
# print(number)
while int(number) > 0:
    summa += int(number) % 10       # складываем все цифры числа между собой
    number = Decimal(number)/10     # Важно, чтобы число после деления оставалось типов Decimal, иначе оно автоматически преобразуется в тип Float 
                                    # и программа начианет работать неправильно
print(summa)