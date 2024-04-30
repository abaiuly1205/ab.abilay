import re

def f(s):
    pattern = r'(?<!^)(?=[A-Z])'
    space = re.sub(pattern, ' ', s)
    return space


s = input()
result = f(s)
print(result)