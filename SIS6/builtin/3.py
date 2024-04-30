def pal_check(str):
    restr = str[::-1]
    return restr == str


str = input()
print(pal_check(str))