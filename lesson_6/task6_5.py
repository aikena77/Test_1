# Жубаева Айкен
# Практическая работа 5
# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра

class Stationery:
    atr_title = 'Title'

    def draw(self):
        print('Start rendering.')


class Pen(Stationery):
    def draw(self):
        print('Pen drawing')


class Pencil(Stationery):
    def draw(self):
        print('Pencil drawing')


class Handle(Stationery):
    def draw(self):
        print('Handle drawing')


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
