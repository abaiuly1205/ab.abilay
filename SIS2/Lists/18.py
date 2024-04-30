def f(n):
    return abs(n - 20)

l = [1, 20, 52, 44, 12, 3]
l.sort(key = f)
print(l)