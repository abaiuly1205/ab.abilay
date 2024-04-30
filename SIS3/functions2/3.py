from d_movies import movies

def categories(c):
    l = []
    for i in movies:
        if i["category"] == c:
            l.append(i["name"])
    print(l)
c = input()
categories(c)