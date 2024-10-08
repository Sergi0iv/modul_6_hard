class Figure:
    sides_count = 0

    def __init__(self, *sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        return valid_types and valid_values

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, *sides, __radius):



    def get_square(self):
        for radius in self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self):
        Figure.__init__(self)

    def get_square(self):
        pass


class  Cube(Figure):
    sides_count = 12

    def __init__(self):
        Figure.__init__(self)

    def get_volume(self):
        pass


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())