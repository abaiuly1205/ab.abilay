def f(str):
    upper = sum(1 for char in str if char.isupper())
    lower = sum(1 for char in str if char.islower())
    return upper, lower

str = input()
upper, lower = f(str)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)