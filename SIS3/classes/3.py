class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__()
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    
shape = Shape()
print(shape.area())

r = Rectangle(int(input()), int(input()))
print(r.area())