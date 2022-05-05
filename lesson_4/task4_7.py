#Жубаева Айкен
# Практическое задание 7
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(num):
    f_num = 1
    if num == 0:
        yield f'{num}! = 1'
    for i in range(1, num + 1):
        f_num *= i
        yield f'{i}! = {f_num}'


for el in fact(int(input('Factorial: '))):
    print(el)
