import os
import json
from random import choice, randint
from datetime import datetime

#python files in our folder
import crud
import model
import server


os.system('dropdb ratings')
os.system('createdb ratings')


model.connect_to_db(server.app)
model.db.create_all()


with open('data/movies.json') as f:
    movie_data = json.loads(f.read()) #movie data is a dictionary

# create_movie(title, overview, release_date, poster_path):
movie_list = []
for data in movie_data:
    title, overview, poster_path = (data['title'],
                                    data['overview'],
                                    data['poster_path'])
    release_date = datetime.strptime(data['release_date'], '%Y-%m-%d')
    movie = crud.create_movie(title, overview, release_date, poster_path)
    # movie = crud.create_movie(data['title'],
    #              data['overview'],
    #              data['release_date'],
    #              data['poster_path'])
    movie_list.append(movie)


for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)

    for _ in range(10):
        random_movie = choice(movie_list)
        score = randint(1,5)

        crud.create_rating(user, random_movie, score)