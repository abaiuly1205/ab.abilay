import re

def f(s):
    pattern = r'\b[a-z]+(?:_[a-z]+)+\b'
    sequences = re.findall(pattern, s)
    return sequences

s = input()
result = f(s)
print(result)