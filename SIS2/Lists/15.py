fruit = ["alma", "almurt", "shie"]
l = []
for x in fruit:
    if "a" in x:
        l.append(x)
print(l)
#*************************************
l = [x for x in fruit if "a" in x]
print(l)
#*************************************
l = [x for x in fruit if x != "shie"]
print(l)
#*************************************
l = [x for x in fruit]
print(l)