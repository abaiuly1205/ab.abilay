def prime(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count == 2

def filter_prime(l):
    res = []
    for x in l:
        if prime(x):
            res.append(x)
    return res

l = map(int, input().split())
print(filter_prime(l))