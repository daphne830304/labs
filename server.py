"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
# Replace this with routes and view functions!

@app.route('/')
def index():
    """Homepage"""

    return render_template('homepage.html')

@app.route('/movies')
def all_movies():
    """Display all movies."""

    movies = crud.get_movies()

    return render_template('all_movies.html', movies= movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie."""
    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie = movie)

@app.route('/users')
def all_users():
    """View users."""

    users = crud.get_users()

    return render_template('all_users.html', users = users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Display users"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/users', methods = ["POST"])
def register_user():

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)
    
    if user:
        flash('email exists')
    else:
        crud.create_user(email,password)
        flash('account created!')

    return redirect('/')


@app.route('/login', methods = ["POST"])
def log_in():

    email = request.form['email']
    password = request.form['password']

    

    user = crud.get_user_by_email(email)
    user_id = user.user_id
   
    print(email)
    print(password)
    print('USER PASSWORD __________________________________________________')
    print(user.password)
    print(user)
    print(type(user))
    print(user_id)


    if password == user.password:
        session["login"] = user_id
        flash('login success')
        
    else:
        flash('Incorrect password')

    return redirect('/')








    # if user:
    #     flash('email exists')
    # else:
    #     crud.create_user(email,password)
    #     flash('account created!')

    # return redirect('/')







if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
