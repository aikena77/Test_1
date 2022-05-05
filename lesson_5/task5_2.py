# Жубаева Айкен
# Практическое задание 2
# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('text_2.txt', 'r', encoding='utf-8') as f:
    my_line = f.readlines()
    for  num_strok, value in enumerate(my_line, 1):
        num_slov = len(value.split())
        print(f' В строке {num_strok} находится {num_slov} слов')