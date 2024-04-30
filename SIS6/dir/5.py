import os

list = ["alma", "almurt", "orik", "zhuzim"]

with open("dir5.txt", "w") as file:
    for i in list:
        file.write(i + "\n")