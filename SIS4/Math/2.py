import math
def area(h, b1, b2):
    area = 1/2 * h * (b1 + b2)
    return area

h = float(input("Enter the height:"))
b1 = float(input("Enter the first base:"))
b2 = float(input("Enter the second base:"))

print(area(h, b1, b2))