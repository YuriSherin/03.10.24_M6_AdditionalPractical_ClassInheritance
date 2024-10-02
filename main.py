import math


class Figure:
    """Базовый класс"""

    def __init__(self, color, *sides, filled=False):
        """Инициализатор родительского класса"""
        if len(sides) == 1:  # Если количество позиционных аргументов == 1
            self.__sides = [sides[0]] * self.sides_count  # генерируем список из длин сторон
        else:
            self.__sides = [1] * self.sides_count  # генерируем список, в котором длины сторон = 1

        if self.__is_valid_color(*color):
            self.__color = list(color)

        self.filled = filled

    def get_color(self):
        """Метод возвращает список RGB цветов"""
        return self.__color

    def __is_valid_color(self, r, g, b):
        """Метод принимает параметры r, g, b, проверяет их корректность
        и возвращает True, если цвета корректны или False"""
        res = True
        rgb = r, g, b  # конвертировали в список
        for color in rgb:
            if isinstance(color, int):
                if 0 <= color <= 255:
                    continue
            res = False
            break
        return res

    def set_color(self, r, g, b):
        """Метод проверяет параметры r, g, b на корректность
        и изменяет атрибут __color на соответствующие значения.
        Если введены некорректные данные, то цвет остаётся прежним."""
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Verify
    def __is_valid_sides(self, *sides: tuple, ):
        """Метод принимает неограниченное кол-во сторон, возвращает True если все стороны
        целые положительные числа и кол-во новых сторон совпадает с текущим,
        False - во всех остальных случаях"""
        res = True
        if len(sides) != len(self.__sides):
            res = False
            return res
        for side in sides:
            if not isinstance(side, int):
                res = False
                break
            if side <= 0:
                res = False
                break
        return res

    def get_sides(self):
        """Метод возвращает значения атрибута __sides"""
        return [*self.__sides]

    def __len__(self):
        """Метод возвращает периметр сторон фигуры"""
        # s = sum(self.__sides)
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        """Метод должен принимать новые стороны.
        Если их количество не равно sides_count, то не изменять,
        в противном случае - менять"""
        lst = [x for x in new_sides if x > 0]
        if len(lst) == self.sides_count:
            self.__sides = lst


class Circle(Figure):
    """Дочерний класс Круг"""
    sides_count = 1

    def __init__(self, color, *sides):
        """Инициализатор дочернего класса"""
        super().__init__(color, *sides)
        self.__radius = self.__len__() / (2 * math.pi)

    def get_square(self):
        """Метод возвращает площадь круга"""
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    """Дочерний класс Треугольник"""
    sides_count = 3

    def get_square(self):
        """Метод возвращает площадь треугольника рассчитать по формуле Герона"""
        p = self.__len__() / 2
        abc = self.get_sides()
        return math.sqrt(p * (p - abc[0]) * (p - abc[1]) * (p - abc[2]))


class Cube(Figure):
    """Дочерний класс Куб"""
    sides_count = 12

    def change_sides(self, side):
        """Метод переопределяет атрибут __sides"""
        self.set_sides(*(side,) * 12)

    def get_volume(self):
        """Метод возвращает объем куба"""
        return self.get_sides()[0] ** 3


# # Код для проверки:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
print(circle1.filled)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
