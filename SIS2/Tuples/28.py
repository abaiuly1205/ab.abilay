cities = ("Almaty", "Astana", "Shymkent")
y = list(cities)
y[1] = "Shu"
cities = tuple(y)
print(cities)
#**************************************
cities = ("Almaty", "Astana", "Shymkent")
y = ("Shu",)
cities += y
print(cities)