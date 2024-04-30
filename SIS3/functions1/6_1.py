def permutations(s):
    l = list(s)
    result = []
    while len(l) > 0:
        current = l.pop()
        print(current)
        if len(current) == len(s):
            result.append(current)
        else:
            for i in range(len(s)):
                if s[i] not in current:
                    l.append(current + s[i])
    return result

s = input()
print(permutations(s))