fruit = ["alma", "almurt", "qyzanaq"]
fruit.remove("qyzanaq")
print(fruit)
#**************************************
fruit = ["alma","qyzanaq", "almurt", "qyzanaq", "shie"]
fruit.remove("qyzanaq")
print(fruit)
#**************************************
fruit = ["alma", "almurt", "shie"]
fruit.pop(1)
print(fruit)
#**************************************
fruit = ["alma", "almurt", "shie"]
fruit.pop()
print(fruit)
#**************************************
fruit = ["alma", "almurt", "shie"]
del fruit[2]
print(fruit)
