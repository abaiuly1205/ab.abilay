fruit = ["alma", "almurt", "shie"]
veg = ["qyzanaq", "kadi", "badiren"]
korzina = fruit + veg
print(korzina)
#**************************************
fruit = ["alma", "almurt", "shie"]
veg = ["qyzanaq", "kadi", "badiren"]

for x in veg:
    fruit.append(x)

print(korzina)
#**************************************
fruit = ["alma", "almurt", "shie"]
veg = ["qyzanaq", "kadi", "badiren"]
fruit.extend(veg)
print(korzina)