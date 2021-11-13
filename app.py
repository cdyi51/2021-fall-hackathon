from datetime import date
from flask import Flask, render_template, request
from helpers import find_pokemon, height, date_spot, favorite_movie, favorite_food, favorite_song, major, user

app: Flask = Flask(__name__)
users: list[user] = []
user_number: int = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        global users
        global user_number

        fname: str = request.form['fname']
        lname: str = request.form['lname']
        height_in_inches: str = request.form['height']
        ideal_date: str = request.form['ideal date']
        food: str = request.form['food']
        movie: str = request.form['movie']
        song: str = request.form['song']
        user_major: str = request.form['major']

        if fname == '' or lname == '':
            return render_template("quiz.html")

        height(int(height_in_inches))
        date_spot(ideal_date)
        favorite_food(food)
        favorite_movie(movie)
        favorite_song(song)
        major(user_major)

        pokemon_result: str = find_pokemon()

        #house: str = find_house(animal)
        new_user: user = user(user_number, fname, lname, pokemon_result)
        users.append(new_user)

        user_number += 1

        return render_template("result.html", pokemon_result = pokemon_result)
    return render_template("quiz.html")


@app.route('/all-results')
def all_results():
    return render_template('all-results.html', users=users)


@app.route('/user<usernumber>')
def display_user(usernumber: str):
    return render_template('user.html', user=users[int(usernumber)])
    

if __name__ == '__main__':
    app.run(debug=True)