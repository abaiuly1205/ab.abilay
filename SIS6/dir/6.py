import os

path = r"/Users/abylay/PP2_ab.abilay/SIS6/new_folder"

for i in range(65,91):
    name = os.path.join(path, chr(i) + ".txt")
    f = open(name, "a")