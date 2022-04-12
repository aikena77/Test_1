# Жубаева Айкен
# Практическое задание 4.

my_str = input("Введите предложение: ")
line = my_str.split(' ')
for ind, el in enumerate(line, 1):
    if len(el) > 10:
        el = el[0:10]
    print("{} {} ".format(ind, el))
