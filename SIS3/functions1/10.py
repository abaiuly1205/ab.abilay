def unique(l):
    new = []
    for i in range(len(l)):
        if l[i] != l[i-1]:
            new.append(l[i])
        elif l[i] == l[i-1]:
            continue
    return new

l = list(map(int, input().split()))
print(unique(l))