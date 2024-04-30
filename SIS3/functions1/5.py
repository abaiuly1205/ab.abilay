def reverse(m):
    s = m[::-1]
    for i in s:
        print(i, end = " ")

m = [i for i in input().split()]

reverse(m)