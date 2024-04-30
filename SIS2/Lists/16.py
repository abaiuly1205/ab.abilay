fruit = ["alma", "almurt", "shie"]
l = [x.upper() for x in fruit]
print(l)
#*************************************
l = [x if x != "shie" else "banan" for x in fruit]
print(l)