user = {}
name=int(input("what is your name: "))
age=int(input("what is age: "))
fav_movie=input("your fav movies: ").split(" ")
fav_songs=input("favorite songs: ").split(" ")

user['name']=name
user['age']=age
user['fav_movie']=fav_movie
user['fav_songs']=fav_songs

for key, value in user.items():
    print(f'{key} : {value}')