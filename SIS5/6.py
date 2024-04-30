import re

def resubing(s):
    pattern = r'[ ,.]'
    res = re.sub(pattern, ':', s)
    return res

s = input()
result = resubing(s)
print(result)