# Жубаева Айкен
# Практическое задание 5.

number = int(input("Введите число "))
my_list = [7, 4, 3, 2]
new_number = my_list.count(number)
for element in my_list:
    if new_number > 0:
        a = my_list.index(number)
        my_list.insert(a + new_number, number)
        break
    else:
        if number > element:
            b = my_list.index(element)
            my_list.insert(b, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
