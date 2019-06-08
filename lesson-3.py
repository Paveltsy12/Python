#Цыганков Павел Владимирович

#easy

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number * (10 ** ndigits) + 0.41
    number = number // 1
    return number / (10 ** ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить



def lucky_ticket(ticket_number):
    num = str(ticket_number)
    lst1 = int(num[:1]) + int(num[1:2])
    lst2 = int(num[-1]) + int(num[-2])
    if lst1 == lst2:
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# def fibonacci(n, m):
#     pass
def fibonacci(n, m):
    a = 0
    b = 1
    c = 0

    for i in range(n):
        if c < m:
            a, b = b, a + b
            print(a)
        c += 1

fibonacci(1,1)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()



def sort_to_max(original_list):
    g = 0
    d = 1
    while d < len(original_list):
        while g < (len(original_list) - 1):
            if original_list[g] > original_list[g + 1]:
                original_list[g], original_list[g + 1] = original_list[g + 1], original_list[g]
            g += 1
        d += 1
        g = 0
    print(original_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_func(function, iterable):
    return (item for item in iterable if function(item))


print(list(filter_func(lambda x: True if 4 < x < 9 else False,
                       [1, 2, 1, 12, 22, 3, 4, 5, 6, 7, 8, 9, 10])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and \
            abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False

print(parallelogram((2, 2), (3, 4), (4, 1), (1, 2)))