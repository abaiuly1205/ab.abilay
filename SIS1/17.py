x = "good"

def f():
    global x
    x = "better"
f()
print("Your life is " + x)