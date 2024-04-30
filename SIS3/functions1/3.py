def solve(numheads, numlegs):
    for x in range(numheads):
        y = numheads - x
        if(2*x + 4*y == numlegs):
            return x, y

numheads = int(input())
numlegs = int(input())

result = solve(numheads, numlegs)
print("Chickens:", result[0])
print("Rabbit:", result[1])