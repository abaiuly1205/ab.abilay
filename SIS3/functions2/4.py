from d_movies import movies

def av(movies):
    sum = 0
    num = 0
    for i in movies:
        sum += i["imdb"]
        num += 1
    print(sum/num)

av(movies)