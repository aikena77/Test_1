 #Жубаева Айкен
# Практическое задание 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

d = dict
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in init_f:
    s