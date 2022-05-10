# Жубаева Айкен
# Практическая работа 2
# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def cals(self):
        print(f"Mass of asphalt - {self._length * self._width * 25 * 5 / 1000}")


def main():
    while True:
        try:
            road_1 = Road(int(input("enter the width of the road in meters: ")),
                          int(input("enter the length of the road in meters: ")))
            road_1.cals()
            break
        except ValueError:
            print("Only integer")


if __name__ == "__main__":
    main()
