from d_movies import movies

def IMDBs(name):
    for movie in movies:
        if name == movie["name"] and movie["imdb"] > 5.5:
            return True
    return False

print(IMDBs(input("Enter name:")))