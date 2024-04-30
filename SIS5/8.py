import re

def upper_split(s):
    pattern = r'[A-Z][a-z]*'
    words = re.findall(pattern, s)
    return words


s = input()
result = upper_split(s)
print(result)