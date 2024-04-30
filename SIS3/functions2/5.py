from d_movies import movies

def categories_av(c):
    sum = 0
    num = 0
    for i in movies:
        if i["category"] == c:
            sum += i["imdb"]
            num += 1
    print(sum/num)

c = input()
categories_av(c)