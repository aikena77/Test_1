my_list = [1, 2, 3, 4,5]
new_list = [el + 10 for el in my_list]
#new_list = [el + 10 for el in my_list if el % 2 == 0]
#new_list = [el + 10 if el % 2 == 0 else el ** 2 for el in my_list ]
print(new_list)