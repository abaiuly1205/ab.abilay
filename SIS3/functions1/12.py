def histogram(l):
    res = ""
    for i in range(len(l)):
        s = ""
        while l[i] > 0:
            s = s + "*"
            l[i] = l[i] - 1
        if i < len(l) - 1:
            res += s + "\n"
        else:
            res += s
    return res

l = list(map(int, input().split()))
print(histogram(l))