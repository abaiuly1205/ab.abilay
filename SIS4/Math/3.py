import math
def polygon_area(n, a):
    area = (n * a**2)/(4 * math.tan(math.pi/n))
    return area
#------------------------------------------------
n = int(input("Enter the number of sides:"))
a = float(input("Enter the length of side:"))
area = round(polygon_area(n, a), 3)

print(area)
#------------------------------------------------