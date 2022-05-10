

def my_func(*args):
    number_1 = int(input("Введите первое число "))
    number_2 = int(input("Введите второе число "))
    number_3 = int(input("Введите третье число "))
    if number_1 >= number_3 and number_2 >= number_3:
        return number_1 + number_2
    elif number_1 > number_2 and number_1 < number_3:
        return number_1 + number_3
    else:
        return number_2 + number_3

if __name__ == "__main__":
    print(my_func())

if __name__ == "__main__":
    print("HI")