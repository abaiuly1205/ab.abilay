a = 7
b = 777
c = 777.01
want = "I want {} shtuk of item nomer {} for {} tenge."
print(want.format(a, b, c))
#******************
want = "I want {1} shtuk of item nomer {0} for {2} tenge."
print(want.format(a, b, c))