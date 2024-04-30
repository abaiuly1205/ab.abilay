class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class square(Shape):
    def __init__(self, l):
        super().__init__()
        self.l = l

    def area(self):
        return self.l ** 2

shape = Shape()
print(shape.area())

square = square(int(input()))
print(square.area())