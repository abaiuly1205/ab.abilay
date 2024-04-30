from d_movies import movies

def sublist(movies):
    l = []
    for i in movies:
        if i["imdb"] > 5.5:
            l.append(i["name"])
    print(l)

sublist(movies)