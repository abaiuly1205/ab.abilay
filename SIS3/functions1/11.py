def pal_chek(s):
    for i in range(len(s)):
        if s[i] == s[len(s) - 1 - i]:
            continue
        else:
            return False
            break 
    return True

s = input()
print(pal_chek(s))