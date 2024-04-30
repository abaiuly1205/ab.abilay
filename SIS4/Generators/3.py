n = int(input())
gen = [i for i in range(n + 1) if i % 3 == 0 and i % 4 == 0]
print(gen)