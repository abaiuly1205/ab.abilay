import re

def m(s):
    p = r"a.*b"
    if re.fullmatch(p, s):
        return True
    else:
        return False

s = input()
if m(s):
    print("String matches the pattern.")
else:
    print("String does not match the pattern.")