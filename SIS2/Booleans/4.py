class v():
    def __len__(self):
        return 0

a = v()
print(bool(a))
#***********************
def f():
    return True

print(f())
#***********************
if f():
    print('YES')
else:
    print('NO')