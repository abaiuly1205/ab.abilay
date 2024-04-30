import re

def f(s):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, s)
    return sequences

s = input()
result = f(s)
print(result)