def p(str):
    def gen(x, y):
        if len(y) == 0:
            print(x)
        else:
            for i in range(len(y)):
                next_char = y[i]
                new = y[:i] + y[i+1:]
                gen(x + next_char, new)
    gen("", str)

str = input()
p(str)